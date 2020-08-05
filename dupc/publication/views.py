from django.shortcuts import render, get_object_or_404,redirect	
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.utils.datastructures import MultiValueDictKeyError
from .models import *

# Create your views here.
def publicationss(request):
	Publication = publication.objects
	return render(request, 'publication/publication.html',{'Publication':Publication})

@login_required(login_url = "/account")
def addpublication(request):
	if request.method == 'POST':
		if request.POST['author'] and request.POST['title'] and request.POST['name'] and request.POST['url'] and request.POST['body']:
			pub = publication()
			if request.POST['gridRadios'] == "1":
				try:
					fm = request.FILES['fl']
				except MultiValueDictKeyError:
					return render(request,'publication/create.html',{'error_message':'Select File Or Change Option'})
				
				pub.pdf = request.FILES['fl']
				pub.has_pdf = True
			else:
				pub.has_pdf = False
			

			pub.authors = request.POST['author']
			pub.title = request.POST['title']
			pub.name = request.POST['name']
			pub.body = request.POST['body']
			pub.link = request.POST['url']
			pub.save()
			return redirect('publication:publication')
		else:
			return render(request,'publication/create.html',{'error_message':'All Field Required'})
	else:
		return render(request,'publication/create.html')
