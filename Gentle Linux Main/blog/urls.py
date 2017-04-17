from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^create/$', views.form_create, name='create'),
    url(r'^(?P<id>\d+)/edit/$', views.update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', views.delete, name='delete'),
]
