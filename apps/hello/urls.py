from django.conf.urls import patterns, url
from apps.hello import views

urlpatterns = patterns('',
    url(r'^requests/$', views.requests_page, name='requests'),
    url(r'^main_page/$', views.main_page, name='main-page'),
)
