from django.conf.urls import patterns, url
from principal.views import verTwitter, listUrl

import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^twitter$', include('twython_django_oauth.urls')),
    url(r'^$', verTwitter),
    url(r'^listar-url/$', listUrl),

    # Media
    url(r'css/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT + '/templates/css'}),
    url(r'images/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT + '/templates/images'}),
    url(r'js/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT + '/templates/js'}),

    # Examples:
    # url(r'^$', 'trabajoConTwitter.views.home', name='home'),
    # url(r'^trabajoConTwitter/', include('trabajoConTwitter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

)
