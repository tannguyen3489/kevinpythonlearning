#from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kevin.views.home', name='home'),
    # url(r'^kevin/', include('kevin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^search/$', 'search.views.search'),
    (r'', include('django.contrib.flatpages.urls')),
)
