from .import views
from django.contrib import admin
from django.urls import path
app_name = 'stories'

urlpatterns = [

    path('',views.stories,name = 'stories'),
    path('add/',views.add,name = 'add'),
] 