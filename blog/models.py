from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

class PostManager(models.Manager):
    def archive(self):
        return 

class Post(models.Model):
    author = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,blank=True,null=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    thumbnail = models.ImageField(blank=True,null=True,upload_to='blog_thumbs',
            help_text='image will be automatically resized')
    body = models.TextField()
    tags = models.CharField(max_length=250,blank=True)
    
    objects = PostManager()

    class Meta:
        verbose_name = 'blog post'
        verbose_name_plural = 'blog posts'

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blog-post', kwargs={
            'year': self.date.year,
            'month': self.date.strftime('%b'),
            'day': self.date.strftime('%d'),
            'slug': self.slug
        })


class Comment(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User,null=True,blank=True)
    ip = models.IPAddressField(blank=True,null=True)
    name = models.CharField(max_length=30,blank=True)
    email =  models.EmailField(blank=True),
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    public = models.BooleanField(default=True)
    spam = models.BooleanField()
