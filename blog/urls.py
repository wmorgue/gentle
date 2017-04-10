from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^about/', views.about, name='about'),
]
