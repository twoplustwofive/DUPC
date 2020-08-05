from django.db import models


class Report(models.Model):
    title = models.CharField(max_length=500)
    name = models.CharField(max_length = 1000,blank = True,default = True)
    date = models.IntegerField(default=12)
    month = models.CharField(max_length=50,default="june")
    year = models.IntegerField(default=2020)
    file = models.FileField(upload_to ='files/')

    def __str__(self):
        return self.title
    