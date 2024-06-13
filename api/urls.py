from django.urls import path
from .views import ProjectsAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    path("projects/", ProjectsAPIView.as_view()),
    path("", get_schema_view(
        info=openapi.Info(
            title="API",
            default_version="v1",
        ),
        public=True
    ).with_ui())
]