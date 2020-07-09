from django.conf.urls import url, include
from .import views
from django.contrib import admin
from django.urls import path
app_name = 'mainsite'
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('teams/',views.teams,name ='teams'),
    path('teams/<int:pk_id>/',views.detail,name = 'detail'),
    path('add/',views.add,name = 'add'),
    path('account/',include('account.urls',namespace='account')),
    path('aim/',views.aim,name = 'aim'),
    path('background/',views.background, name = 'background'),
    path('activities/',views.activity,name = 'activity'),
    path('teams/anamika/' ,views.anamika,name  = 'anamika'),
    path('teams/<int:pk_id>/remove/',views.remove,name = 'remove'),
    path('contact/',views.contact,name = 'contact'),
]