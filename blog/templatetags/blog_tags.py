from django.template import Library

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
