from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from .models import podcast


def outreach(request):
    pc = podcast.objects
    return render(request,'outreach/outreach.html',{'pc':pc})


@login_required
def addpod(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['detail'] and request.POST['date'] and request.POST['month'] and  request.POST['year'] and request.POST['url']:
            pc = podcast()
            pc.title = request.POST['title']
            pc.date = request.POST['date']  
            pc.body = request.POST['detail']
            pc.month = request.POST['month']
            pc.year = request.POST['year']
            pc.url = request.POST['url']
            pc.save()
            return redirect('outreach:outreach')
        else:
            return render(request,'outreach/out.html',{'error_message': 'ALL Fields Required !'})   
    else:
        return render(request,'outreach/out.html')