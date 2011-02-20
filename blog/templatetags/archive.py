from django.template import Library
from blog.models import Post
from django.utils.datastructures import SortedDict
from django.conf import settings
register = Library()

@register.inclusion_tag('blog/includes/archive.html')
def archive():
    month_fmt = getattr(settings, 'BLOG_ARCHIVE_MONTH_FORMAT', '%B');
    posts = SortedDict()
    for post in Post.objects.order_by('date'):
        year = post.date.year
        if not posts.get(year):
            posts[year] = {}
        if not posts[year].get('months'):
            posts[year]['months'] = SortedDict()
        if not posts[year].get('count'):
            posts[year]['count'] = 0
        month = post.date.strftime(month_fmt)
        if not posts[year]['months'].get(month):
            posts[year]['months'][month] = []
        posts[year]['months'][month].append(post)
        posts[year]['count'] += 1
        
    #sort years descending
    posts.keyOrder = sorted(posts.keyOrder, reverse=True)
    return {'archive':posts}
