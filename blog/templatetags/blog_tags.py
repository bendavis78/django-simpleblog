from django.template import Library, Node, TemplateSyntaxError
from blog.models import Post
import re

register = Library()

@register.filter
def get_author_name(user):
    if user.first_name and user.last_name:
        f = '%(first_name)s %(last_name)s'
    elif user.first_name:
        f = '%(first_name)s'
    else:
        f = '%(username)s'
    return f % user.__dict__

class RecentPostsNode(Node):
    def __init__(self, num_posts, varname):
        self.num_posts = num_posts
        self.varname = varname

    def render(self, context):
        posts = Post.objects.all().order_by('-date')[:self.num_posts]
        context[self.varname] = posts
        return ''

@register.tag
def get_recent_posts(parser, token):
    """
    {% get_recent_posts %}
    {% get_recent_posts <num_posts> %}
    {% get_recent_posts as <varname> %}
    {% get_recent_posts <num_posts> as <varname> %}
    {% get_recent_posts as <varname> <num_posts> %}
    """
    bits = token.contents.split()
    num_posts = None
    varname = 'posts'
    if 'as' in bits:
        try:
            varname = bits[bits.index('as')+1]
        except IndexError:
            raise TemplateSyntaxError('"as" must be followed by a variable name')
    if len(bits) == 2:
        num_posts = bits[2]
    elif len(bits) == 4:
        if bits[1] == 'as':
            num_posts = bits[3]
        if bits[2] == 'as':
            num_posts = bits[1]
    elif len(bits) > 4:
        raise TemplateSyntaxError('Invalid number of arguments for get_recent_posts')
    if not num_posts:
        num_posts = 5
    return RecentPostsNode(num_posts, varname)
