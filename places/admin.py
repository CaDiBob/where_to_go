from django.contrib import admin
from places.models import Places, Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('object_id', 'places')
    list_display_links = ('places',)
    ordering = ('object_id',)

admin.site.register(Places)
