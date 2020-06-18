from django.conf.urls import url, include
from .import views
from django.contrib import admin
from django.urls import path

app_name = 'news'

urlpatterns = [
    path('',views.newss,name = 'news'),
    path('add/',views.addnews,name = 'add'),
]
