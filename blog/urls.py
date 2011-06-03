from django.conf.urls.defaults import patterns, url
from blog.models import Post
from blog.views import ArchiveCategoryView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DateDetailView
from blog.feeds import LatestEntriesFeed

info = {
    'model': Post,
    'date_field': 'date',
}

urlpatterns = patterns('', 
    url(r'^$', ArchiveIndexView.as_view(**info), name='blog-index'),
    url(r'^feed/$', LatestEntriesFeed(), name='blog-feed'),
    url(r'^(?P<year>\d{4})/$', YearArchiveView.as_view(**info), name='blog-archive-year'),
    url(r'^(?P<year>\d{4})/(?P<month>[A-z]{3})/$', MonthArchiveView.as_view(**info), name='blog-archive-month'),
    url(r'^(?P<category>[\w-]+)/$', ArchiveCategoryView.as_view(**info), name='blog-archive-category'),
    url(r'^(?P<year>\d{4})/(?P<month>[A-z]{3})/(?P<day>\d+)/(?P<slug>.+)/$',  DateDetailView.as_view(**info), name='blog-post'),
)
