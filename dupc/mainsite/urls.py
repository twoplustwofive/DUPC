from django.conf.urls import url, include

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
<<<<<<< HEAD
    path('teams/',views.teams,name ='teams'),
=======
    path('login',views.loginpage,name='loginpage'),
    path('logout',views.Logout,name='logoutpage'),
>>>>>>> 5523bb73da3963818eaffeed754f5219dfe1b8e1
]