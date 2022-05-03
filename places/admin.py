from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.utils.html import format_html

from places.models import Places, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('object_id', 'places',)
    list_display_links = ('places',)
    ordering = ('object_id', )


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    list_display = ('image', 'object_id')
    fields = ('object_id', 'image', 'place_images')
    readonly_fields = ('place_images',)
    ordering = ('object_id', )

    def place_images(self, object):
        if object.image:
            return format_html(f'<img src="{object.image.url}" height="200px" />')

    place_images.short_description = 'Миниатюра'


@admin.register(Places)
class PlacesAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ('title',)
    ordering = ('pk',)
    inlines = [ImageInline]
