# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import team


# Create your views here.


def homepage(request):
    return render(request,'index.html')



def teams(request):    
    tm = team.objects
    return render(request,'teams.html',{'tm':tm})

@login_required(login_url = "/account")
def add(request):
    if request.method == 'POST':
        
        
        if request.POST['name'] and request.POST['email'] and request.POST['phone'] and  request.POST['body'] and request.FILES['img']:
            tm = team()
            tm.name = request.POST['name']
            tm.email_id = request.POST['email']  
            tm.phone = request.POST['phone']
            tm.information = request.POST['body']
            tm.image = request.FILES['img']
            tm.save()
            return redirect('mainsite:teams')
        else:
            return render(request, 'addteam.html',{'error_message':'All fields are required.'})
    else:
        return render(request,'addteam.html')

def background(request):
    return render(request,'background.html')



def aim(request):
    return render(request,'aim.html')


def activity(request):
    return render(request,'base.html')


def detail(request,pk_id):
    member = get_object_or_404(team,pk = pk_id)
    return render(request,'detail.html',{'member': member}) 
    

@login_required(login_url = "/account")
def remove(request,pk_id):
    member = get_object_or_404(team,pk = pk_id)
    member.delete()
    return redirect('mainsite:teams')