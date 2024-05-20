from django.shortcuts import render
from django.views.generic import ListView
from .models import Project
# Create your views here.

class ProjectsList(ListView):
    template_name = "projects.html"
    model = Project
    queryset = Project.objects.all()
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topic"] = "All"
        return context


class TechnologyProjectsList(ListView):
    template_name = "projects.html"
    model = Project
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.filter(technologies__slug=self.kwargs["slug"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topic"] = self.kwargs["slug"]
        return context


class CategoryProjectsList(ListView):
    template_name = "projects.html"
    model = Project
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.filter(category__slug=self.kwargs["slug"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topic"] = self.kwargs["slug"]
        return context