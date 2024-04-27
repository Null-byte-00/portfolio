from django.shortcuts import render
from django.views.generic import ListView
from .models import Article
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

