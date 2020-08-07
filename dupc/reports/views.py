from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from .models import Report

def reports(request):
    rp = Report.objects.filter().order_by('-id')

    return render(request,'reports/reports.html',{'rp':rp})

@login_required(login_url = "/account")
def add(request):
    if request.method == 'POST':
        
        
        if request.POST['title'] and request.POST['date'] and request.POST['date'] and request.POST['month'] and request.POST['year'] and request.POST['author']:
            try:
                fm = request.FILES['fl']
            except MultiValueDictKeyError:
                return render(request, 'reports/create.html',{'error_message':'All fields are required.'})
                
            rp = Report()
            rp.title = request.POST['title']
            rp.date = request.POST['date']
            rp.month = request.POST['month']
            rp.name = request.POST['author']
            rp.year = request.POST['year']
            rp.file = request.FILES['fl']
            rp.save()
            return redirect('reports:reports')
        else:
            return render(request, 'reports/create.html',{'error_message':'All fields are required.'})
    else:
        return render(request,'reports/create.html')