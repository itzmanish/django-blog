from django.shortcuts import render
from .models import Article


def blog(request):
    articles = Article.objects
    return render(request, 'blog.html', {'articles': articles})
