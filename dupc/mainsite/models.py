from __future__ import unicode_literals

from django.db import models

class team(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'images/', default = 'download.png')
    designation = models.CharField(max_length = 1500, default= None)
    institute_name = models.CharField(max_length = 1500,default = 'IITG',blank=True)
    department = models.CharField(max_length=1500,default = 'HSS',blank=True)
    information = models.TextField(max_length = 3000, default= None)
    
    def __str__(self):
        return self.name

    def ida(self):
        return self.name[:2]
    