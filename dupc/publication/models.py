from django.db import models

# Create your models here.
class publication(models.Model):
	authors = models.CharField(max_length=1200)
	title = models.CharField(max_length=1000)
	name = models.CharField(max_length=700)
	pdf = models.FileField(upload_to='files/',blank=True)
	link = models.CharField(max_length=500,blank=True)
	has_pdf = models.BooleanField(default=False)
	body = models.TextField(max_length=5000,default=False)
	
	def __str__(self):
		return self.title
