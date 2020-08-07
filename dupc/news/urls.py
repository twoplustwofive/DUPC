from django.conf.urls import url, include
from .import views
from django.contrib import admin
from django.urls import path

app_name = 'news'

urlpatterns = [
    path('',views.newss,name = 'news'),
    path('<int:year>/<str:month>/',views.nss,name = 'nss'),
    path('add/',views.addnews,name = 'add'),
    path('addupdate/',views.addupdate,name = 'addupdate'),
    path('<int:pk_id>/', views.detail, name = 'detail'),
]
