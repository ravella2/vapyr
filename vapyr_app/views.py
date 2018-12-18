from django.shortcuts import render, redirect
from .models import Game, UserProfile, JoinTable
from vapyr_app.forms import UserForm, UserProfileForm
from django.contrib.auth.models import User
import requests
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
<<<<<<< HEAD
=======
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'vapyr_app/registration.html', {'user_form':user_form,'profile_form':profile_form,'registered':registered})

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
>>>>>>> 95d0bd39917dc4b69a2d91b1915476a9fc9f80df

