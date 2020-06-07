from django.contrib import admin

# Register your models here.

from .models import Job,category

admin.site.register(Job)
admin.site.register(category)
