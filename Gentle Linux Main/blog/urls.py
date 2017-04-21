from django.conf.urls import url


from . import views
from .views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<id>\d+)/$', DetailView.as_view(), name='detail'),
    url(r'^create/$', CreateView.as_view(), name='create'),
    # url(r'^(?P<id>\d+)/edit/$', EditView.as_view(), name='update'),
    url(r'^(?P<id>\d+)/edit/$', views.edit, name='update'),
    url(r'^(?P<id>\d+)/delete/$', views.delete, name='delete'),
]
#
