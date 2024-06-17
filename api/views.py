from django.shortcuts import render
from .serializers import ProjectSerializer, ArticleSerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from mainapp.models import Resume, Experience, SiteDescription
from projects.models import Project
from articles.models import Article
# Create your views here.


class OverallAPIView(APIView):
    def get(self,request):
        return Response({
            "resume": Resume.objects.first().resume,
            "site_description": SiteDescription.objects.first().about,
            "experience": Experience.objects.first().experience
        })


class ProjectsAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ArticleAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer






