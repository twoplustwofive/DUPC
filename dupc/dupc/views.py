from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def loginn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                return redirect('mainsite:homepage')
            else:
               return render(request,'registration/login.html',{'error_message':'Invalid Password.'})
        else:
           return render(request,'registration/login.html',{'error_message':'Invalid Username or Password.'})
    form = AuthenticationForm()
    return render(request,'login.html')