# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import team
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.


def homepage(request):
    return render(request,'index1.html')



def teams(request):    
    tm = team.objects
    return render(request,'teams.html',{'tm':tm})

@login_required(login_url = "/account")
def add(request):
    if request.method == 'POST':
        
        
        if request.POST['name'] and request.POST['designation'] and request.POST['body'] and request.POST['institute_name'] and request.POST['department']:
            try:
                fm = request.FILES['img']
            except MultiValueDictKeyError:
                return render(request, 'addteam.html',{'error_message':'All fields are required.'})
                
            tm = team()
            tm.name = request.POST['name']
            tm.designation = request.POST['designation']
            tm.information = request.POST['body']
            tm.image = request.FILES['img']
            tm.institute_name = request.POST['institute_name']
            tm.department = request.POST['department']
            tm.save()
            return redirect('mainsite:teams')
        else:
            return render(request, 'addteam.html',{'error_message':'All fields are required.'})
    else:
        return render(request,'addteam.html')

def background(request):
    return render(request,'background1.html')



def aim(request):
    return render(request,'aim.html')


def activity(request):
    return render(request,'activity.html')


def detail(request,pk_id):
    member = get_object_or_404(team,pk = pk_id)
    return render(request,'detail.html',{'member': member}) 

def anamika(request):
    return render(request,'detail_anamika.html')
    

@login_required(login_url = "/account")
def remove(request,pk_id):
    member = get_object_or_404(team,pk = pk_id)
    member.delete()
    return redirect('mainsite:teams')


def contact(request):
    return render(request,'contact.html')