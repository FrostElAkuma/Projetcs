from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required

from .models import User, category, listing, bid, comment
from .forms import createListing, createBiding, addComment

def index(request):
    return render(request, "auctions/index.html", {
        #excluding inactive listings
        "listings": listing.objects.exclude(active=False),
        #i am using this categories so the category drop down list works 
        "categories": category.objects.all()
    })

#this was given to me
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

#this was given to me
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

#this was given to me
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):
    if request.method == "POST":
        form = createListing(request.POST)
        if form.is_valid():
            
            wtv = form.save(commit=False) # do not commit it yet (save in db)
            #i need the user but i cant fill it in the html so i fill it here before submiting it to the db
            wtv.poster = request.user
            wtv.save()
            
            #another way
            '''
            user = request.user
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            start = form.cleaned_data['startPrice']
            image = form.cleaned_data['image']
            categorized = form.cleaned_data['categorized']

            wtv = listing(poster=user, title=title, description=description, startPrice=start, image=image, categorized=categorized)
            wtv.save()
            '''

        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/createlist.html", {
            'form': createListing(),
            "categories": category.objects.all()
        })

@login_required
def listing_page(request, listing_id):
    listingInfo = listing.objects.get(pk=listing_id)
    #if there is a bid already
    if listingInfo.currentBid:
        minAmount = listingInfo.currentBid
    #if this is the first bid to be made
    else:
        minAmount = listingInfo.startPrice
    if request.method == "POST":
        #this took me 4 hours to figure out. needed the minAmount for validation to be inside the createBiding()
        form = createBiding(minAmount, request.POST)
        if form.is_valid():
            new = form.save(commit=False) 
            listingInfo.currentBid = new.bidAmount
            listingInfo.save()
            new.bidder = request.user
            new.auction = listing.objects.get(pk=listing_id)
            new.save()
            return HttpResponseRedirect(reverse("listing_page", kwargs={'listing_id': listing_id}))
        return HttpResponseRedirect(reverse("listing_page", kwargs={'listing_id': listing_id}))
        

    else:
        user = request.user
        #to make sure that the user is the owner of the post
        if listingInfo.poster == request.user:
            deactivate = True
        else:
            deactivate = False
        #if there is a bid already
        if listingInfo.currentBid:
            minAmount = listingInfo.currentBid
        #if this is the first bid to be made
        else:
            minAmount = listingInfo.startPrice
        #if the user has this already in his watching list
        if request.user in listingInfo.watchedBy.all():
            flag = True

        else:
            flag = False

        return render(request, "auctions/lpage.html", {
            "listing": listingInfo,
            "user": user,
            "watch": flag,
            "form": createBiding(minAmount),
            "deactivate": deactivate,
            "commentForm": addComment(),
            #getting all the comments for this listing 
            "allComments": comment.objects.filter(listComments = listing_id),
            "categories": category.objects.all()
            })
     
def editWatch(request, listing_id, route):
    post = listing.objects.get(pk=listing_id)
    if request.user in post.watchedBy.all():
        post.watchedBy.remove(request.user)

    else:
        post.watchedBy.add(request.user)
    #if he using the add / remove from watch list button from the listing page
    if route == 1:
        return HttpResponseRedirect(reverse("listing_page", kwargs={'listing_id': listing_id}))
    #if he using the remove button from the watchlist page
    else:
        return HttpResponseRedirect(reverse("watchList"))
        
def watchList(request):
    userWatchList = request.user.watching.all()
    return render(request, "auctions/watchlist.html", {
                "list": userWatchList,
                "categories": category.objects.all()
            })

def deactivate(request, listing_id):
    listingInfo = listing.objects.get(pk=listing_id)
    bidInfo = bid.objects.get(auction=listing_id, bidAmount=listingInfo.currentBid)
    #to make sure that the user is the owner of the post. So other users wont be able to access this url and deactivate the listing 
    if listingInfo.poster == request.user:
        winner = bidInfo.bidder
        listingInfo.active = False
        listingInfo.winner = winner
        listingInfo.save()
        
    return HttpResponseRedirect(reverse("index"))

def commento(request, listing_id):
    if request.method == "POST":
        form = addComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.commentor = request.user
            comment.listComments = listing.objects.get(pk=listing_id)
            comment.save()
            return HttpResponseRedirect(reverse("listing_page", kwargs={'listing_id': listing_id}))

#1 hour wasted to fix dropdown. At the end i needed to delete 2 letters cuz of bootstrap version diffrences :))
def categori(request, category_name):
    if category_name == "all":
        return render(request, "auctions/category.html", {
        "categories": category.objects.all()
    })
    else:
        cate = category.objects.get(name=category_name)
        cate_id = cate.id
        listingInfo = listing.objects.filter(categorized=cate_id, active=True)
        return render(request, "auctions/fIndex.html", {
        "listings": listingInfo,
        "categories": category.objects.all()
    })