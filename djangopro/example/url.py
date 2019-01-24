from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.main, name='main',),
    url(r'^index/$', views.index, name='index',),
    url(r'^contact/$', views.contact, name='contact', ),
    url(r'^about/$', views.about, name='about', ),
    url(r'^gallery/$', views.gallery, name='gallery', ),
    url(r'^main/$', views.main, name='main',),
]