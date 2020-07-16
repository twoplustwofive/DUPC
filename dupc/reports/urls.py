from django.conf.urls import url, include
from .import views
from django.contrib import admin
from django.urls import path

app_name = 'reports'

urlpatterns = [
    path('',views.reports,name = 'reports'),
    path('add/',views.add,name = 'add'),
]