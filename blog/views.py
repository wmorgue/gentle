from django.shortcuts import render
from django.utils import timezone


from .models import Post


def home(request):
    template = 'blog/home.html'
    return render(request, template)


def index(request):
    item = Post.objects.all()
    context = {'item': item}
    return render(request, 'blog/index.html', context)


def detail(request):
    context = {'item': item}
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html')
