from urllib.parse import quote_plus
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect


from .forms import PostForm
from .models import Post


def index(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 5)
    page_var = "p"
    page = request.GET.get(page_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {'page_var': page_var, 'object_list': queryset, 'title': 'List'}
    return render(request, 'blog/index.html', context)


def form_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Successfully Created YO')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {"form": form}
    return render(request, 'blog/form_create.html', context)


def detail(request, id=None):
    obj = get_object_or_404(Post, id=id)
    share_string = quote_plus(obj.text)
    context = {'obj': obj, 'share_string': share_string}
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
    return render(request, 'blog/form_create.html', context)


def delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, 'Successfully deleted')
    return redirect('blog:index')
