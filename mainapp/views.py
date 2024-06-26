from django.shortcuts import render
from .models import SiteDescription, Media, Resume, Biography, Experience
from articles.models import Article
from projects.models import Project
import markdown
# Create your views here.


def home(request):
    site_description = SiteDescription.objects.first()
    new_articles = Article.objects.all().order_by("-date")[:3]
    new_projects = Project.objects.all().order_by("-date")[:3]
    media = Media.objects.all()
    return render(request, "home.html", {"site_description": site_description, 
                                         "medias": media,
                                         "new_articles": new_articles,
                                         "new_projects": new_projects})


def about(request):
    site_description = SiteDescription.objects.first().about
    md = markdown.Markdown(extensions=["fenced_code"])
    site_description = md.convert(site_description)
    return render(request, "about.html", {"about": site_description})


def experience(request):
    experience = Experience.objects.first()
    md = markdown.Markdown(extensions=["fenced_code"])
    experience.experience = md.convert(experience.experience)
    return render(request, "experience.html", {"experience": experience})


def resume(request):
    resume = Resume.objects.first()
    md = markdown.Markdown(extensions=["fenced_code"])
    resume.resume = md.convert(resume.resume)
    return render(request, "resume.html", {"resume": resume})