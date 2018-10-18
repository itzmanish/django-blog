from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.details, name='details'),
]
