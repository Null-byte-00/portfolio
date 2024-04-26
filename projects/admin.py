from django.contrib import admin

# Register your models here.

from .models import Category, Technology, Project

admin.site.register(Category)
admin.site.register(Technology)
admin.site.register(Project)