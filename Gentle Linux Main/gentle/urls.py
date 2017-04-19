"""gentle URL Configuration"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='gentle/home.html'), name='home'),
    url(r'^about/', TemplateView.as_view(template_name='gentle/about.html'), name='about'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
