import urllib.parse
from django.http import HttpResponseRedirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CreateForm
from .models import Post


def index(request):
    queryset_list = Post.objects.active()
    paginator = Paginator(queryset_list, 3)
    page_var = "p"
    page = request.GET.get(page_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {'page_var': page_var, 'object_list': queryset}
    return render(request, 'blog/index.html', context)


def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(obj.get_absolute_url())
    else:
        form = CreateForm()
    context = {"form": form}
    return render(request, 'blog/create.html', context)


def detail(request, id=None):
    obj = get_object_or_404(Post, id=id)
    share_string = urllib.parse.quote_plus(obj.text)
    context = {'obj': obj, 'share_string': share_string}
    return render(request, 'blog/detail.html', context)


def update(request, id=None):
    obj = get_object_or_404(Post, id=id)
    form = CreateForm(request.POST or None, request.FILES or None, obj=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(obj.get_absolute_url())
    context = {"title": obj.title, "obj": obj, "form": form}
    return render(request, "blog/detail.html", context)


def delete(request):
    obj = get_object_or_404(Post, id=id)
    obj.delete()
    return redirect('blog:index')
