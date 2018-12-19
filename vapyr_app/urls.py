from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/user/<username>/', views.show, name='show'),
    path('user_login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='user_logout'),
    path('special',views.special, name='special'),
    path('register',views.register, name='register'),
    path('profile/<username>', views.new_profile, name="new_profile"),
    path('move_game',views.move_game, name='move_game')
]

