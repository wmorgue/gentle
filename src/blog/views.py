import urllib.parse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .forms import CreateForm
from .models import Post

class IndexView(View):
    """Simple page pagination."""
    @staticmethod
    def get(request, template='blog/index.html'):
        queryset_list = Post.objects.active()
        query = request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(title__icontains=query)
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
        return render(request, template, context)


class CreateView(View):
    template = 'blog/create.html'
    form_class = CreateForm
    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template, context)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return redirect(obj.get_absolute_url())
        context = {'form': form}
        return render(request, self.template, context)


class DetailView(View):
    @staticmethod
    def get(request, template='blog/detail.html', id=None):
        obj = get_object_or_404(Post, id=id)
        share_string = urllib.parse.quote_plus(obj.text)
        context = {'obj': obj, 'share_string': share_string}
        return render(request, template, context)


def edit(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = CreateForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute_url())
    context = {'title': instance.title, 'instance': instance, 'form': form}
    return render(request, "blog/create.html", context)


def delete(request, id=None):
    obj = get_object_or_404(Post, id=id)
    obj.delete()
    return redirect('blog:index')
