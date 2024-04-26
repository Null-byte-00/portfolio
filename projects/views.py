from django.shortcuts import render
from django.views.generic import ListView
from .models import Project
# Create your views here.

class ProjectsList(ListView):
    template_name = "projects.html"
    model = Project
    queryset = Project.objects.all()
    context_object_name = "projects"
