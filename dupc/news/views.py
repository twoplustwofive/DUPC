from django.shortcuts import render
from .models import news

# Create your views here.
def newss(request):
    News = news.objects
    return render(request,'news/news.html',{'News':News})