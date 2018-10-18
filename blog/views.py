from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article


def blog(request):
    articles = Article.objects.all()
    return render(request, 'blog.html', {'articles': articles})


def details(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'single_post.html', {'article': article})
