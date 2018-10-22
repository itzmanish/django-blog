from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article


def blog(request):
    if request.user.is_authenticated:
        articles = Article.objects.all()
        context = {'articles': articles}
        return render(request, 'blog.html', context)

    return render(request, 'blog.html',)


def details(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'single_post.html', {'article': article})
