from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from .import views
app_name = "account"

urlpatterns = [
    path('',views.loginpage,name='loginpage'),
    path('logout/',views.Logout,name='logoutpage'),
    
    
    
]+  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

