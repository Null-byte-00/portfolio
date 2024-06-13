from django.shortcuts import render
from .serializers import ProjectSerializer
from rest_framework.generics import ListAPIView
from projects.models import Project
# Create your views here.


class ProjectsAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



