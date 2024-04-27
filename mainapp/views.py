from django.shortcuts import render
from .models import SiteDescription, Media, Resume, Biography, Experience
import markdown
# Create your views here.

def home(request):
    site_description = SiteDescription.objects.first()
    media = Media.objects.all()
    return render(request, "home.html", {"site_description": site_description, "medias": media})


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