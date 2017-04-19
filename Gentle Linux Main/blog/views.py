import urllib.parse
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
            return redirect(obj.get_absolute_url())
    else:
        form = CreateForm()
    context = {"form": form}
    return render(request, 'blog/create.html', context)


def detail(request, id=None):
    obj = get_object_or_404(Post, id=id)
    share_string = urllib.parse.quote_plus(obj.text)
    context = {'obj': obj, 'share_string': share_string}
    return render(request, 'blog/detail.html', context)


def edit(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = CreateForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute_url())
    context = {'title': instance.title, 'instance': instance, 'form': form}
    # obj_var = get_object_or_404(Post, id=id)
    # form = CreateForm(request.POST or None, request.FILES or None, obj_var=obj_var)
    # if form.is_valid():
    #     obj_var = form.save(commit=False)
    #     obj_var.save()
    #     return redirect(obj_var.get_absolute_url())
    # context = {"title": obj_var.title, "obj_var": obj_var, "form": form}
    return render(request, "blog/create.html", context)


def delete(request, id=None):
    obj = get_object_or_404(Post, id=id)
    obj.delete()
    return redirect('blog:index')
