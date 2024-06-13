from django.urls import path
from .views import ProjectsAPIView


urlpatterns = [
    path("projects/", ProjectsAPIView.as_view())
]