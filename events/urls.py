from django.conf.urls import patterns, include, url

urlpatterns = patterns('events.views',
    url(r'^create/$', 'create_event', name='create_event'),
)