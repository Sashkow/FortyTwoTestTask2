from django.conf.urls import patterns, url
from apps.hello import views

urlpatterns = patterns('',
    url(r'^$', views.main_page, name='main-page'),
)