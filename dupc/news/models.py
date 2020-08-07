from django.db import models


class news(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField(max_length = 3000 ,default= None)
    url = models.CharField(max_length=500)
    date = models.IntegerField(default=12)
    month = models.CharField(max_length=50,default="june")
    year = models.IntegerField(default=2020)
    file = models.FileField(upload_to ='files/')
    has_url = models.BooleanField(default = True)
    has_file = models.BooleanField(default = True)

    def summary(self):
        return self.body[:250]


class update(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField(max_length = 3000 ,default= None)
    url = models.CharField(max_length=500,blank = True)
    date = models.IntegerField(default=12)
    month = models.CharField(max_length=50,default="june")
    year = models.IntegerField(default=2020)
    file = models.FileField(upload_to ='files/')
    image = models.ImageField(upload_to = 'images/',blank  = True)
    has_url = models.BooleanField(default = True)
    has_file = models.BooleanField(default = True)
    has_image = models.BooleanField(default = False)

    def __str__(self):
        return self.title

    def recent(self):
        return self.update[:5]
    