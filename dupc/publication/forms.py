from django import forms
from .models import *

class publicationform(forms.ModelForm):
	class Meta:
		model = publication
		fields = '__all__'
		widgets = {
			'authors' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add all authors separated by ,'}),
			'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of Publication'}),
			'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of Publication'}),
			'pdf' : forms.FileInput(attrs={'class':'form-control', 'placeholder':'Title of Publication'}),
			'link' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Insert Link'}),
		}