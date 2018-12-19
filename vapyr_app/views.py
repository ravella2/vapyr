from django.shortcuts import render, redirect
from .models import Game, UserProfile, JoinTable
from vapyr_app.forms import UserForm, UserProfileForm
from django.contrib.auth.models import User
import requests
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'vapyr_app/main.html' )

def show(request, username):
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user_id=user)
    games = JoinTable.objects.filter(userKey=profile)
    return render(request, 'vapyr_app/profile.html', {'user':user, 'games':games, 'profile':profile})
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return redirect('profile/'+user.username)
        else:
            print(user_form.errors)
            return render(request, 'vapyr_app/registration.html', {'user_form':user_form}, {'error':'invalid'})
    else:
        user_form = UserForm()
        return render(request, 'vapyr_app/registration.html', {'user_form':user_form})

def new_profile(request, username):
    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST)
        if profile_form.is_valid():
            profile_form['user_id'].initial = request.user
            profile = profile_form.save()
            return redirect('user/'+username)
        
            # if 'profile_pic' in request.FILES:
            #     profile.profile_pic = request.FILES['profile_pic']
            # profile.save()
        else:
            print(profile_form.errors)
    else:
        profile_form = UserProfileForm()
        if(username):
            return render(request, 'vapyr_app/new_profile.html', {'profile_form':profile_form, 'registered': True})
        else:
            return render(request, 'vapyr_app/new_profile.html', {'profile_form':profile_form, 'registered': False})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print(f'They used username: {username} and password: {password}')
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'vapyr_app/login.html', {})

def move_game(request):
    
    game_id = request.GET['game_id']
    print(game_id)
    return HttpResponse(request, 'vapyr_app/profile.html')


