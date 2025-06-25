from django.shortcuts import render
from django.views.generic import ListView
from .models import Article


class ListArticlesView(ListView):
    model = Article
    template_name = 'blog/articles.html'
    context_object_name = 'articles'
