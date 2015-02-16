from django.conf.urls import patterns, include, url

#import ds.utils
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jproj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', ds.views.view..),

    # url(r'^admin/', include(admin.site.urls)),
)
