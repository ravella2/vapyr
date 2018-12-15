from django.contrib import admin
from .models import UserProfile, Game, JoinTable
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Game)
admin.site.register(JoinTable)