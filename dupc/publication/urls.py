from .import views
from django.contrib import admin
from django.urls import path

app_name = 'publication'

urlpatterns = [
	path('',views.publicationss,name='publication'),
	path('add/',views.addpublication,name='add'),
]