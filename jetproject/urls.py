from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jetproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^jetapp/', include('jetapp.urls')),
                       
                       
    url(r'^signup/', 'login.views.signup'), #tugrul
                       
                       
    url(r'^home/', 'login.views.home'), #tugrul
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
