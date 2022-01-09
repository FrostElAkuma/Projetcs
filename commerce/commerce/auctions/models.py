from django.contrib.auth.models import AbstractUser
from django.db import models

#this was given to me already
class User(AbstractUser):
    pass
#category model that has an image and a name
class category(models.Model):
    img = models.URLField(blank=True, max_length=200)
    name = models.CharField(max_length=20)
#self is the pk (priamry key)
    def __str__(self):
	    return f"{self.name}"
#some times i need to use null=True and blank=True if i add more variables after i already migrated
class listing(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=40)
    description =  models.CharField(max_length=200)
    startPrice =  models.DecimalField(max_digits=6, decimal_places=0)
    currentBid = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=0)
    image = models.URLField(blank=True, max_length=300)
    watchedBy = models.ManyToManyField(User, blank=True, related_name="watching")
    #replies = models.ForeignKey(comment, on_delete=models.CASCADE, related_name="reply") #thought i wanted to link the comments with the listing but guess there was no reason  
    categorized = models.ForeignKey(category, null=True, blank=True, on_delete=models.CASCADE, related_name="categories")
    winner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="won")
    
    def __str__(self):
	    return f"{self.id}: {self.title} ({self.startPrice})"

class bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    auction = models.ForeignKey(listing, on_delete=models.CASCADE, related_name="currentBider")#?
    bidAmount = models.DecimalField(max_digits=6, decimal_places=0)

    def __str__(self):
	    return f"{self.auction}: {self.bidAmount}"

class comment(models.Model):
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listComments = models.ForeignKey(listing, on_delete=models.CASCADE, related_name="commentSection")#?
    commento = models.CharField(max_length=200)

    def __str__(self):
	    return f"{self.listComments}: {self.commento}"  

