from __future__ import unicode_literals

from django.db import models

class team(models.Model):
    name = models.CharField(max_length = 30)
    email_id = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 15)
    image = models.ImageField(upload_to = 'images/', default = 'download.png')
    information = models.TextField(max_length = 300)
    
    def __str__(self):
        return self.name
    