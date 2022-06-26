from re import template
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = "posts/home.html"