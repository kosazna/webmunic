from django.shortcuts import render
from .models import Post


def home(response):
    context = {
        'posts': Post.objects.all()
    }
    return render(response, "blog/home.html", context)


def about(response):
    return render(response, "blog/about.html", {'title': 'About'})
