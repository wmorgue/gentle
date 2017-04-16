"""gentle URL Configuration"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='gentle/home.html'), name='home'),
    url(r'^about/', TemplateView.as_view(template_name='gentle/about.html'), name='about'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^admin/', admin.site.urls),
]
