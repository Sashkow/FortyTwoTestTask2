from django.conf.urls import patterns, include, url

from django.contrib import admin
from apps.hello import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', include('apps.hello.urls')),
    url(r'^$', views.main_page, name='main-page'),
)
