from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^blog/', views.index, name='index'),
    url(r'^blog/(?P<item>[0-9]+)/$', views.detail, name='detail'),
]
