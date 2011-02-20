# Create your views here.
from django.views.generic.dates import ArchiveIndexView

class ArchiveCategoryView(ArchiveIndexView):
    template_name_suffix = '_archive_category'

    def get_queryset(self):
        category = self.kwargs.get('category')
        return self.model.objects.filter(category=category)
