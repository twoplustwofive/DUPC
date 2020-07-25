from django.db import models

class Story(models.Model):
    name = models.CharField(max_length = 1000)
    title = models.CharField(max_length = 1000)
    url = models.CharField(max_length = 1000)
    body = models.CharField(max_length=5000, default=None)
