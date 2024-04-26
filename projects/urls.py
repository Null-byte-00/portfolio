from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path("", views.ProjectsList.as_view(), name="projects"),
]