from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('user/<slug:username>/', views.show, name='show'),

]

