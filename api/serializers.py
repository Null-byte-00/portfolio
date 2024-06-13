from rest_framework import serializers
from projects.models import Project
from articles.models import Article
from mainapp.models import SiteDescription, Resume, Experience


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'link', 'category', 'technologies', 'date']