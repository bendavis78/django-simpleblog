from django.contrib.syndication.views import Feed
from blog.models import Post

class LatestEntriesFeed(Feed):
    title = 'Capstone.MD Blog'
    link = '/blog/'
    description_template = 'blog/includes/feed_description.html'

    def items(self):
        return Post.objects.order_by('-date')[:20]

    def item_title(self, item):
        return item.title
