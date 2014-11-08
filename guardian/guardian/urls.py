from django.conf.urls import patterns, include, url

from django.contrib import admin
import crime_stats.views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guardian.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'crime_stats.views.home', name='home'),
    url(r'^assets', 'crime_stats.views.assets', name='assets')
)
