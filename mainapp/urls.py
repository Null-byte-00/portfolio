from django.urls import path
from . import views

app_name = "mainapp"

urlpatterns = [
    path("", views.home),
    path("about/", views.about, name="about"),
    path("experience/", views.experience, name="experience"),
    path("resume/", views.resume, name="resume"),
]