from django.conf.urls import url, include
from .import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('teams',views.teams,name ='teams'),
    path('login',views.loginpage,name='loginpage'),
    path('logout',views.Logout,name='logoutpage'),
]