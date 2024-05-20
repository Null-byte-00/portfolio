from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path("", views.ProjectsList.as_view(), name="projects"),
    path("technology/<slug:slug>/", views.TechnologyProjectsList.as_view(), name="technology"),
    path("category/<slug:slug>/", views.CategoryProjectsList.as_view(), name="category"),
]