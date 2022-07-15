from django.contrib import admin

from Workspace.models import student

from .models import Products
# Register your models here.
admin.site.register(Products)

admin.site.register(student)