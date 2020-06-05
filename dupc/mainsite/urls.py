from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('login',views.loginpage,name='loginpage'),
    path('logout',views.Logout,name='logoutpage'),
]