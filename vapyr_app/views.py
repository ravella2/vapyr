from django.shortcuts import render, redirect
from .models import Game, UserProfile, JoinTable
from vapyr_app.forms import UserForm, UserProfileForm, GameForm
from django.contrib.auth.models import User
import requests
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    return render(request, 'vapyr_app/main.html' )


@csrf_exempt
def game_create(request, title):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save() 
            join_table = JoinTable.objects.get_or_create(userKey=request.user.profile, gameKey=game, prefer=True, wishlist=False)
            return HttpResponse(request.user.username)
        else:
            game = Game.objects.get(title=title)
            join_table = JoinTable.objects.get_or_create(userKey=request.user.profile, gameKey=game, prefer=True, wishlist=False)   
            return HttpResponse(request.user.username)
    return HttpResponse('')

@csrf_exempt
def game_wish(request, title):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save()
            join_table = JoinTable.objects.get_or_create(userKey=request.user.profile, gameKey=game, prefer=False, wishlist=True)
            # games = JoinTable.objects.filter(userKey=request.user.profile)
            return HttpResponse(request.user.username)
        else:
            game = Game.objects.get(title=title)
            join_table = JoinTable.objects.get_or_create(userKey=request.user.profile, gameKey=game, prefer=True, wishlist=False)   
            return HttpResponse(request.user.username)
    return HttpResponse('')

@csrf_exempt
def game_list_toggle(request, pk):
    game = JoinTable.objects.get(pk=pk)
    game.prefer = not game.prefer
    game.wishlist = not game.wishlist
    game.save()
    user = request.user.username
    return redirect('show', username = user)

@csrf_exempt
def edit_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == "POST":
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
    return render(request, 'vapyr_app/registration.html', {'user_form':user_form})

def new_profile(request, username):
    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST)
        if profile_form.is_valid():
            profile_form['user_id'].initial = request.user
            profile = profile_form.save(commit=False)
            ids = [{"console": "Switch", "gid": 157}, {"console": "PS4", "gid": 146}, {"console": "PC", "gid": 94}, {"console": "XboxOne", "gid": 145}]
            setID = 'no pref'
            for di in ids :
                print(di)
                for key in di :
                    print(di[key])
                    if di[key] == profile.pref_platform :
                        setID = di['gid']
                        print('HERE IS THE ID')
                        print(setID)
                        profile.pref_plat_id = setID
            profile.save()
            return redirect('user/'+username)
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
        print('test')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('profile/user/'+username) 
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print(f'They used username: {username} and password: {password}')
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'vapyr_app/login.html', {})
