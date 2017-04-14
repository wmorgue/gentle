from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


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
        messages.success(request, 'Successfully Created YO')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, 'Not Created')
    context = {"form": form}
    return render(request, 'blog/form_create.html', context)


def detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {'title': instance.title, 'instance': instance}
    return render(request, 'blog/detail.html', context)


def update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Update Saved')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {'title': instance.title, 'instance': instance, 'form': form}
    return render(request, 'blog/detail.html', context)


def about(request):
    return render(request, 'blog/about.html')
