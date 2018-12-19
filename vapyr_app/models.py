from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    pref_platform = models.CharField(max_length=100)
    GAMER_STYLES = (
        ('CASUAL', 'Casual'),
        ('HARDCORE', 'Hardcore'),
        ('PRO', 'Profesional')
    )
    gamer_style = models.CharField(max_length=11, choices=GAMER_STYLES, default='HARDCORE')

    def __str__(self):
        return self.user_id.username

class Game(models.Model):
    title = models.CharField(max_length=100, unique = True)
    image = models.URLField(blank=True, max_length=150)
    platform = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    rating = models.SmallIntegerField()

    def __str__(self):
        return self.title


class JoinTable(models.Model):
    userKey = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='users')
    gameKey = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='games')
    prefer = models.BooleanField()
    wishlist = models.BooleanField()
    
    def __str__(self):
        return self.userKey.user_id.username + " " + self.gameKey.title


