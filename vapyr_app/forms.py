from django import forms
from vapyr_app.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password','email')

GAMER_STYLES = (
    ('CASUAL', 'Casual'),
    ('HARDCORE', 'Hardcore'),
    ('PRO', 'Profesional')
)
class UserProfileForm(forms.ModelForm):
    gamer_style= forms.CharField(label='What is your gaming style?', widget=forms.Select(choices=GAMER_STYLES))


    class Meta():
        model = UserProfile
        fields = ('user_id','gamer_style','pref_platform','profile_pic')