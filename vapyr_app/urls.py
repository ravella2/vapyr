from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/user/<username>/', views.show, name='show'),
    path('user_login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='user_logout'),
    path('special',views.special, name='special'),
    path('game/create', views.game_create, name='game_create'),
    path('game/wish', views.game_wish, name='game_wish'),
    path('register',views.register, name='register'),
    path('profile/<username>', views.new_profile, name="new_profile"),
    path('game/<int:pk>/edit', views.edit_game, name='edit_game'),
    path('game/<int:pk>/delete', views.delete_game, name='delete_game'),
]

