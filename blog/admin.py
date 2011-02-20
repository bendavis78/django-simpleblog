from django.contrib import admin
from django.db.models import TextField
from blog import models
from tinymce.widgets import TinyMCE

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {TextField:{'widget':TinyMCE(attrs={'cols':100,'rows':30})}}
    list_display = ['title', 'date']
    date_hierarchy = 'date'
    list_filter = ['category']


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Post, PostAdmin)
