from django.db import models

# Create your models here.
class podcast(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField(max_length = 3000 ,default= None)
    url = models.CharField(max_length=500)
    date = models.IntegerField(default=12)
    month = models.CharField(max_length=50,default="june")
    year = models.IntegerField(default=2020)
    image = models.ImageField(upload_to = 'images/',default = 'download.png')
    
    def __str__(self):
        return self.title


class media(models.Model):
    title = models.CharField(max_length = 500,blank = True)
    body = models.TextField(max_length = 3000 ,default= None)
    url = models.CharField(max_length=500)
    image = models.ImageField(upload_to = 'images/',default = 'download.png')
    
    def __str__(self):
        return self.title