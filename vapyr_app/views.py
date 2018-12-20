from django.shortcuts import render, redirect
from .models import Game, UserProfile, JoinTable
from vapyr_app.forms import UserForm, UserProfileForm, GameForm
from django.contrib.auth.models import User
import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    return render(request, 'vapyr_app/main.html' )


@csrf_exempt
def game_create(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save()
            join_table = JoinTable.objects.get_or_create(userKey=request.user.profile, gameKey=game, prefer=True, wishlist=False)
            games = JoinTable.objects.filter(userKey=request.user.profile)    
            return HttpResponse(request.user.username)
    return HttpResponse('')

@csrf_exempt
def game_wish(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save()
            join_table = JoinTable.objects.get_or_create(userKey=request.user.profile, gameKey=game, prefer=False, wishlist=True)
            games = JoinTable.objects.filter(userKey=request.user.profile)
            return HttpResponse(request.user.username)
    return HttpResonse('')


@csrf_exempt
def edit_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == "POST":
        print('HEPL ME PLZ')
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            game = form.save()
            return redirect('show', username=request.user.username)
    else:
        form = GameForm(instance=game)
    return render(request, 'vapyr_app/editform.html', {'form': form})


@csrf_exempt
def delete_game(request, pk):
    Game.objects.get(id=pk).delete()
    return redirect('show', username=request.user.username)

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
                return redirect('show')
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


