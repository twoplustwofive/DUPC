from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.utils.datastructures import MultiValueDictKeyError
from .forms import *
from .models import *

# Create your views here.
def publicationss(request):
	Publication = publication.objects.filter(admin_approved=True)
	return render(request, 'publication/publication.html',{'Publication':Publication})

@login_required(login_url = "/account")
def addpublication(request):
	if request.method=='POST':
		pubform = publicationform(request.POST)
		if pubform.is_valid():
			pubform.save()
			pubform = publicationform()
			allpubs = publication.objects.filter(admin_approved=True)
			return render(request, 'publication/create.html', {'pubform':pubform, 'allpubs':allpubs})

		else:
			pubform = publicationform()
			allpubs = publication.objects.filter(admin_approved=True)
			return render(request, 'publication/create.html', {'pubform':pubform, 'allpubs':allpubs})

	else:
		pubform = publicationform()
		allpubs = publication.objects.filter(admin_approved=True)
		return render(request, 'publication/create.html', {'pubform':pubform, 'allpubs':allpubs})