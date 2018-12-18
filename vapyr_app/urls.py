from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('user/<username>/', views.show, name='show')
]

