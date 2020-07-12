from django.conf.urls import url, include
from .import views
from django.contrib import admin
from django.urls import path

app_name = 'outreach'

urlpatterns = [
    path('',views.outreach,name = 'outreach'),
    path('add/',views.addpod,name = 'addpod'),
    
]
