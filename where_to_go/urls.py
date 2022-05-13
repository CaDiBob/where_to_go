from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.urls import re_path

from django.views.static import serve

from places import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_palaces, name='mainpage'),
    path('places/<int:place_id>', views.show_place, name='places'),
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
