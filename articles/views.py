from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article
import markdown
# Create your views here.

class ArticlesList(ListView):
    template_name = "articles.html"
    context_object_name = "articles"
    model = Article
    ordering = ["-date"]
    paginate_by = 2
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Articles"
        return context


class ArticleDetail(DetailView):
    template_name = "article.html"
    context_object_name = "article"
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        md = markdown.Markdown(extensions=["fenced_code"])
        context["body"] = md.convert(self.get_object().body)
        return context
    
    def get_object(self) -> Model:
        return self.model.objects.get(slug=self.kwargs.get("slug"))
