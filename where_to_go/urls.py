from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls import re_path
from django.views.static import serve

from places import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_palaces, name='mainpage'),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
