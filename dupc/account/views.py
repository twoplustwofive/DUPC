from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def loginpage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request,"You are now logged in as {username}")
                return redirect('mainsite:homepage')
            else:
               return render(request,'login.html',{'error_message':'Invalid Password.'})
        else:
           return render(request,'login.html',{'error_message':'Invalid Username or Password.'})
    form = AuthenticationForm()
    return render(request,'login.html')

def Logout(request):
    logout(request)
    return redirect('mainsite:homepage')