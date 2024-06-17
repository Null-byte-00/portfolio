from django.urls import path
from .views import ProjectsAPIView, ArticleAPIView, OverallAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    path("projects/", ProjectsAPIView.as_view()),
    path("articles/", ArticleAPIView.as_view()),
    path("overall_data/", OverallAPIView.as_view()),
    path("", get_schema_view(
        info=openapi.Info(
            title="API",
            default_version="v1",
        ),
        public=True
    ).with_ui())
]