from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import django.contrib.auth
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^test/$', 'login.views.jet'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^initiation/', include('initiation.urls')),
     url(r'^$', 'initiation.views.trending',
                           name='trending'),
                       # the three feed pages
                       url(r'^feed/$',
                           'initiation.views.feed', name='feed'),
                       url(r'^aggregated_feed/$',
                           'initiation.views.aggregated_feed', name='aggregated_feed'),
                       # a page showing the users profile
                       url(r'^profile/(?P<username>[\w_-]+)/$',
                           'initiation.views.profile', name='profile'),
                       # backends for follow and pin
                       url(r'^pin/$',
                           'initiation.views.pin', name='pin'),
                       url(r'^follow/$',
                           'initiation.views.follow', name='follow'),
                       # the admin
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^auth/', include('django.contrib.auth.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
                           url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                               {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                           url(r'', include(
                               'django.contrib.staticfiles.urls')),
                           ) + urlpatterns

# make sure we register verbs when django starts
from initiation import verbs