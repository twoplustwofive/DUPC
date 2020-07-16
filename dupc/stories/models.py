from django.db import models

class Story(models.Model):
    name = models.CharField(max_length = 1000)
    title = models.CharField(max_length = 1000)
    url = models.CharField(max_length = 1000)
    image = models.ImageField(upload_to = 'images/')
