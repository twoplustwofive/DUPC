from django.contrib import admin

# Register your models here.
from .models import news,update
admin.site.register(news)
admin.site.register(update)