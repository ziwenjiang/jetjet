from django.conf.urls import patterns, url
from initiation import views

urlpatterns = patterns('',
        url(r'^$', views.index, name ='index'))