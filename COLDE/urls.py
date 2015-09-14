#encoding:utf8
"""COLDE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from articles.views import RSSFeed


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
  	url(r'^$','articles.views.home',name="home"),
    url(r'^article/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<id>\d+)/$', 'articles.views.detail', name="detail"),
    url(r'^article/(?P<year>\d{4})/(?P<month>\d{1,2})/$','articles.views.archive_month',name="archive_month"),
    url(r'^archive/$','articles.views.archive',name="archive"),
    url(r'^about/$', 'articles.views.about', name="about"),
    url(r'^message/$', 'articles.views.message', name="message"),
    url(r'^tag/(?P<tag>\w+)', 'articles.views.tag', name="tag"),
    url(r'^category/(?P<category>\w+)', 'articles.views.category', name="category"),
    url(r'^search/$', 'articles.views.search', name="search"),
    url(r'^rss/$', RSSFeed(), name='rss'),
]

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)