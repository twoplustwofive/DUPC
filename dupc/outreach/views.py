from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError


def outreach(request):
    return render(request,'outreach/outreach.html')


@login_required
def addpod(request):
    return render(request,'outreach/out.html')