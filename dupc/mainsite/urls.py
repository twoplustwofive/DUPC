from django.conf.urls import url, include
from .import views
from django.contrib import admin
from django.urls import path
app_name = 'mainsite'
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('teams/',views.teams,name ='teams'),
    path('add/',views.add,name = 'add'),
    path('account/',include('account.urls',namespace='account')),
]