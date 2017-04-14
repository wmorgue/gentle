from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^blog/', views.index, name='index'),
    url(r'^create/$', views.form_create, name='create'),
    url(r'^(?P<id>\d+)/edit/$', views.update, name='update'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
]
