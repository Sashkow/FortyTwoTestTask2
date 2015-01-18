from django.conf.urls import patterns, url
from apps.hello import views

urlpatterns = patterns('',
    url(r'^requests/$', views.requests, name='requests'),
    url(r'^main/$', views.main, name='main'),
    url(r'^edit/$', views.edit, name='edit'),
)
