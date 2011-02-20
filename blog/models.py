from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'

class PostManager(models.Manager):
    def archive(self):
        return 

class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,blank=True,null=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField()
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

