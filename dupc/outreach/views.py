from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from .models import podcast,media


def outreach(request):
    pc = podcast.objects
    md = media.objects
    return render(request,'outreach/outreach.html',{'pc':pc,'md':md})


@login_required
def addpod(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['detail'] and request.POST['date'] and request.POST['month'] and  request.POST['year'] and request.POST['url']:
            try:
                fm = request.FILES['img']
            except MultiValueDictKeyError:
                return render(request,'outreach/out.html',{'error_message': 'ALL Fields Required !'})

            pc = podcast()
            pc.title = request.POST['title']
            pc.date = request.POST['date']  
            pc.body = request.POST['detail']
            pc.month = request.POST['month']
            pc.year = request.POST['year']
            pc.url = request.POST['url']
            pc.image = request.FILES['img']
            pc.save()
            return redirect('outreach:outreach')
        else:
            return render(request,'outreach/out.html',{'error_message': 'ALL Fields Required !'})   
    else:
        return render(request,'outreach/out.html')

@login_required
def addmedia(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['detail'] and request.POST['url']:
            try:
                fm = request.FILES['img']
            except MultiValueDictKeyError:
                return render(request,'outreach/addmedia.html',{'error_message': 'ALL Fields Required !'})

            md = media()
            md.title = request.POST['title']
            
            md.body = request.POST['detail']
            
            md.url = request.POST['url']
            md.image = request.FILES['img']
            md.save()
            return redirect('outreach:outreach')
        else:
            return render(request,'outreach/addmedia.html',{'error_message': 'ALL Fields Required !'})   
    else:
        return render(request,'outreach/addmedia.html')