from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index, name='index', ),
    path('profile/user/<username>/', views.show, name='show'),
    path('user_login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='user_logout'),
    path('special',views.special, name='special'),
    path('game/create/<title>', views.game_create, name='game_create'),
    path('game/wish/<title>', views.game_wish, name='game_wish'),
    path('game/list/<int:pk>', views.game_list_toggle, name="game_list_toggle"),
    path('register',views.register, name='register'),
    # path('profile/<username>', views.new_profile, name="new_profile"),
    path('game/<int:pk>/edit', views.edit_game, name='edit_game'),
    path('game/<int:pk>/delete', views.delete_game, name='delete_game'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)