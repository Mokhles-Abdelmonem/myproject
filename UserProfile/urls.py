from django.urls import path
from . import views



urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('settings/', views.settings, name='settings'),
    path('sendingmail/', views.sendingmail, name='sendingmail'),
    path('changepassword/<token>/', views.changepassword, name='changepassword'),
	path('search_profile', views.search_profile, name='search_profile'),
    path('logout/' , views.Logout , name="logout"),

]
