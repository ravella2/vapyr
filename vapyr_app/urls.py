from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('user/<username>/', views.show, name='show'),
    path('user_login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='user_logout'),
    path('special',views.special, name='special'),
]

