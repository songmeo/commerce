from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import User, Auction


def index(request):
    return render(request, "auctions/index.html", {
        "auctions": Auction.objects.all()
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


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

categories = (
    (1, "Fashion"),
    (2, "Toys"),
    (3, "Electronics"),
    (4, "Home"),
    (5, "Others")
)

class CreateListingForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(
        widget=forms.Textarea()
    )
    starting_bid = forms.FloatField()
    image = forms.URLField(required=False)
    category = forms.TypedChoiceField(choices = categories,
                                    coerce = str 
                                    )

@login_required
def create(request):
    if request.method == "POST":
        form = CreateListingForm(request.POST)
        if form.is_valid():
            new_listing = Auction()
            new_listing.name = form.cleaned_data['name']
            new_listing.description = form.cleaned_data['description']
            new_listing.price = form.cleaned_data['starting_bid']
            new_listing.image = form.cleaned_data['image']
            new_listing.category = form.cleaned_data['category']
            new_listing.save()
            return render(request, "auctions/listing.html", {
                "listing": new_listing
            })
    return render(request, "auctions/create.html", {
        "form": CreateListingForm()
    })

def listing(request, id):
    listing = Auction.objects.get(id=id)
    print(listing.name)
    return render(request, "auctions/listing.html", {
        "listing": listing
    })