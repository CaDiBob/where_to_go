from django.contrib import admin
from places.models import Places, Image

from django.utils.html import format_html



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('object_id', 'places',)
    list_display_links = ('places',)
    ordering = ('object_id', )


class ImageInline(admin.TabularInline):
    model = Image
    fields = ('image', 'place_images', 'object_id')
    readonly_fields = ('place_images',)

    def place_images(self, obj):
        return format_html(f'<img src="{obj.image.url}" height="200px" />')
    place_images.short_description = 'Image'

@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
