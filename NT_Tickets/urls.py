from django.conf.urls import patterns, include, url
import settings
import tickets.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^book/(?P<show_id>\d+)/$', 'tickets.views.book_landing', name='book'),
    url(r'^book/(?P<show_id>\d+)/thanks/$', 'tickets.views.book_finish', name='finish'),
    url(r'^book/(?P<show_id>\d+)/error/$', 'tickets.views.book_error', name='error'),
    url(r'^cancel/(?P<ref_id>.*)/$', 'tickets.views.cancel', name='cancel'),
    url(r'^list/$', tickets.views.ListShows.as_view(), name='list'),
    url(r'^list/(?P<slug>[-_\w]+)/$', tickets.views.DetailShow.as_view(), name='detail'),
    url(r'^sidebar/$', 'tickets.views.sidebar', name='sidebar'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns