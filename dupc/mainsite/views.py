# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.


def homepage(request):
    return render(request,'index.html')



def teams(request):    
    return render(request,'teams.html')


