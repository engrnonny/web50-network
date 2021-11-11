

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *


def index(request):
    posts = Post.objects.all().order_by('-date_added')
    context = {
        'posts': posts
    }
    return render(request, "network/index.html", context)


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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


# New Post
# New Post
# New Post
@login_required
def new_post(request):
    if request.method == "POST":
        body = request.POST["body"]
        if body:
            post = Post(body=body, user=request.user)
            post.save()
            return redirect("index")
        else:
            pass


# User Profile Page
# User Profile Page
# User Profile Page
@login_required
def user_profile(request, slug):
    profile_user = User.objects.get(username=slug)
    if profile_user:
        try:
            posts = Post.objects.filter(user=profile_user).order_by('-date_added')
            followee = Follower.objects.get(user=profile_user)
            followers = len(User.objects.filter(followers__id=followee.id))
            following = len(User.objects.filter(following__id=followee.id))
            followed = User.objects.filter(followers__id=followee.id, id=request.user.id)
            
            context = {
                'followed': followed,
                'followers': followers,
                'following': following,
                'posts': posts,
                'profile_user': profile_user
            }
        except IntegrityError:
            pass
        return render(request, "network/user-profile.html", context)
        

    else:
        pass

    
# Follow and unfollow
# Follow and unfollow
# Follow and unfollow
@login_required
def follow_or_unfollow(request, slug):
    followee = User.objects.get(username=slug)
    follower = User.objects.get(username=request.user)

    # Checks that the current user's profile isn't the profile to be followed.
    if followee == follower:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    # Checks that the followee (current profile being viewed), has a Follower object
    elif Follower.objects.filter(user=followee).exists():
        follow = Follower.objects.get(user=followee)
        followed = User.objects.filter(followers__id=follow.id)

        # Follows or unfollows the followee
        if followed:
            follow.followers.remove(follower)
        else:
            follow.followers.add(follower)

        # Checks that the follower (current logged in user), has a Follower object
        if Follower.objects.filter(user=follower).exists():
            following = Follower.objects.get(user=follower)
            followed = User.objects.filter(following__id=following.id, id=followee.id)

            # Adds or removes the followee
            if followed:   
                following.following.remove(followee)
            else:
                following.following.add(followee)
            
        # Creates a Follower object if none exist for the follower
        else:
            follow = Follower(user=follower)
            follow.save()
            follow.following.add(followee)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    # Creates a Follower object if none exist for the followee
    else:
        follow = Follower(user=followee)
        follow.save()
        follow.followers.add(follower)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
