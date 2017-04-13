from django.shortcuts import render, get_object_or_404
from django.utils import timezone


from .forms import PostForm
from .models import Post


def home(request):
    return render(request, 'blog/home.html')


def index(request):
    queryset = Post.objects.all()
    context = {'object_list': queryset, 'title': 'List'}
    return render(request, 'blog/index.html', context)


def form_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form": form,
    }
    return render(request, 'blog/form_create.html', context)


def detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {'title': instance.title, 'instance': instance}
    return render(request, 'blog/detail.html', context)


def about(request):
    return render(request, 'blog/about.html')
