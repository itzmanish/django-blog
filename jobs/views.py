from django.shortcuts import render
from .models import Job


def Home(request):
    jobs = Job.objects
    return render(request, 'home.html', {'jobs': jobs})
