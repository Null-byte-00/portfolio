from rest_framework import serializers
from projects.models import Project
from articles.models import Article
from mainapp.models import SiteDescription, Resume, Experience


class ProjectSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
     )
    
    technologies = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
    
    class Meta:
        model = Project
        fields = ['title', 'description', 'link', 'category', 'technologies', 'date']


class ArticleSerializer(serializers.ModelSerializer):
    serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )

    class Meta:
        model = Article
        fields = ['title', 'body', 'date', 'tags', 'slug']