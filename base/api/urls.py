from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^accounts/', include('accounts.api.urls')),
    url(r'^events/', include('events.api.urls')),
    # url(r'^polls/', include('polls.api.urls')),
    # url(r'^conversations/', include('conversations.api.urls')),
)
