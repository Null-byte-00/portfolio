from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.ArticlesList.as_view(), name="articles"),
    #path("<slug:slug>/", views.ArticleDetail.as_view(), name="article"),
]