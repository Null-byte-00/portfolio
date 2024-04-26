from django.shortcuts import render
from .models import SiteDescription, Media
# Create your views here.

def home(request):
    site_description = SiteDescription.objects.first()
    media = Media.objects.all()
    return render(request, "home.html", {"site_description": site_description, "medias": media})