from django.shortcuts import render, redirect
from .models import Game, UserProfile, JoinTable
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
import requests

# Create your views here.

def index(request):
    return render(request, 'vapyr_app/main.html' )

def show(request, username):
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user_id=user)
    games = JoinTable.objects.filter(userKey=profile)
    return render(request, 'vapyr_app/profile.html', {'user':user, 'games':games, 'profile':profile})
