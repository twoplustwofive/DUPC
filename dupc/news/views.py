from django.shortcuts import render
from .models import news,update
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def newss(request):
   
    up = update.objects.filter().order_by('-id')
    
    return render(request,'news/news.html',{'up':up})


def nss(request,year,month):
   
    Ns = news.objects.filter(year = year)
    News = Ns.filter(month = month)
    
    return render(request,'news/news_display.html',{'News':News})




@login_required(login_url = "/account")
def addnews(request):
    if request.method == 'POST':
        
        
        if request.POST['title'] and request.POST['detail'] and request.POST['date'] and request.POST['month'] and  request.POST['year']:
            ns = news()
            if request.POST['gridRadios1'] == "1" and request.POST['url']:
                ns.url = request.POST['url']
                ns.has_url = True
            elif request.POST['gridRadios1'] == "1":
                return render(request, 'news/create.html',{'error_message':'Url required. or Change Has Url Option'})
            else:
                ns.has_url = False

            if request.POST['gridRadios'] == "1":
                try:
                    fm = request.FILES['fl']
                except MultiValueDictKeyError:
                    return render(request, 'news/create.html',{'error_message':'File required. or Change Has File Option'})
                ns.file = request.FILES['fl']
                ns.has_file = True
            else:
                ns.has_file = False
                
            
            ns.title = request.POST['title']
            ns.date = request.POST['date']  
            ns.body = request.POST['detail']
            ns.month = request.POST['month']
            ns.year = request.POST['year']
            ns.save()
            return redirect('news:news')
        else:
            return render(request, 'news/create.html',{'error_message':'All fields are required.'})
    else:
        return render(request,'news/create.html')


def detail(request,pk_id):
    ns = get_object_or_404(news,id = pk_id)
    return render(request,'news/detail.html',{'ns':ns})


@login_required(login_url = "/account")
def addupdate(request):
    if request.method == 'POST':
        
        
        if request.POST['title'] and request.POST['detail'] and request.POST['date'] and request.POST['month'] and  request.POST['year']:
            ns = update()
            if request.POST['gridRadios1'] == "1" and request.POST['url']:
                ns.url = request.POST['url']
                ns.has_url = True
            elif request.POST['gridRadios1'] == "1":
                return render(request, 'news/create.html',{'error_message':'Url required. or Change Has Url Option'})
            else:
                ns.has_url = False

            if request.POST['gridRadios'] == "1":
                try:
                    fm = request.FILES['fl']
                except MultiValueDictKeyError:
                    return render(request, 'news/create.html',{'error_message':'File required. or Change Has File Option'})
                ns.file = request.FILES['fl']
                ns.has_file = True
            else:
                ns.has_file = False
            
            if request.POST['gridRadios3'] == "1":
                try:
                    fm1 = request.FILES['img']
                except MultiValueDictKeyError:
                    return render(request, 'news/create_update.html',{'error_message':'Image required. or Change Has Image Option'})
                ns.image = request.FILES['img']
                ns.has_image = True
            else:
                ns.has_image = False
            
                
            
            ns.title = request.POST['title']
            ns.date = request.POST['date']  
            ns.body = request.POST['detail']
            ns.month = request.POST['month']
            ns.year = request.POST['year']
            ns.save()
            return redirect('news:news')
        else:
            return render(request, 'news/create_update.html',{'error_message':'All fields are required.'})
    else:
        return render(request,'news/create_update.html')
