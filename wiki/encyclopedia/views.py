from django.shortcuts import render
from django import forms
#from django.forms import TextInput, Textarea
from django.http import HttpResponseRedirect
from django.urls import reverse

import markdown2
import secrets

from . import util

class AddEntry(forms.Form):
    hName = forms.CharField(label="Title", widget=forms.TextInput(attrs={'class' : 'form-control col-sm-7 col-lg-7'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control col-sm-7 col-lg-7', 'rows' : 5}))
    flag = forms.BooleanField(initial=False, widget=forms.HiddenInput(), required=False)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, name):
    if(util.get_entry(name)):
        markdowner = markdown2.Markdown()
        return render(request, "encyclopedia/main.html", {
            "entry": markdowner.convert(util.get_entry(name)),
            "title": name
        })
    else:
        return render(request, "encyclopedia/main.html", {
            "entry": False,
            "title": name
        })

def search(request):
    input = request.GET.get('q', '')
    if(util.get_entry(input)):
        #return HttpResponseRedirect(reverse("url name from urls.py", kwargs={'the arguement that the url takes': the value for that arguement}))
        return HttpResponseRedirect(reverse("title", kwargs={'name': input}))
    
    else:
        scramble = []
        for wtv in util.list_entries():
            if input.lower() in wtv.lower():
                scramble.append(wtv)
        return render(request, "encyclopedia/index.html", {
            "entries": scramble
        })

def create(request):
    if request.method == "POST":
        form = AddEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data["hName"]
            text = form.cleaned_data["content"]
            if(util.get_entry(title) == None or form.cleaned_data["flag"] == True):
                util.save_entry(title, text)
                return HttpResponseRedirect(reverse("title", kwargs={'name': title}))

            else:    
                return render(request, "encyclopedia/create.html", {
                    #sending back the sumbited form with the input data
                    "form": form,
                    "error": 1
                })

        else:
            return render(request, "encylopedia/create.html", {
                "form": form,
                "error": 2
            })

    else:
        return render(request, "encyclopedia/create.html", {
            "form": AddEntry()
        })

def edit(request, name):
    if util.get_entry(name):
        #we render the edit page and fill the form based on the name of the
        #entry that was given
        form = AddEntry()
        form.fields["hName"].initial = name
        #we hide the title so the user cant change it
        form.fields["hName"].widget = forms.HiddenInput()
        form.fields["content"].initial = util.get_entry(name)
        form.fields["flag"].initial = True
        return render(request, "encyclopedia/create.html", {
            "form": form,
            "title": name,
            "flag": True       
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "title": name
        })
#;)))
def ashwai(request):
    random = util.list_entries()
    choseRandom = secrets.choice(random)
    #trying out redirect
    return HttpResponseRedirect(reverse("title", kwargs={'name': choseRandom}))