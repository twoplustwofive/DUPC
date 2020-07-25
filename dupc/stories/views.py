from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from .models import Story

# Create your views here.
def stories(request):
    st = Story.objects

    return render(request,'stories/stories.html',{'st':st})


@login_required(login_url = "/account")
def add(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['name'] and request.POST['url'] and request.POST['body']:
            sr = Story()
            sr.title = request.POST['title']
            sr.name = request.POST['name']
            sr.url = request.POST['url']
            sr.body = request.POST['body']
            sr.save()
            return redirect('stories:stories')
        else:
            return render(request,'stories/create.html',{'error_message':'All fields are required.'})
    else:
        return render(request,'stories/create.html')

