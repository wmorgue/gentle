from django.shortcuts import render


def home(request):
    return render(request, 'blog/home.html')


def blog(request):
    return render(request, 'blog/blog.html')


def about(request):
    return render(request, 'blog/about.html')
