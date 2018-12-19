from django import forms
from vapyr_app.models import UserProfile, Game
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileForm(forms.ModelForm):

    class Meta():
        model = UserProfile
        fields = ('gamer_style','pref_platform','profile_pic')

class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields= ('title', 'image', 'platform', 'genre', 'description', 'rating')