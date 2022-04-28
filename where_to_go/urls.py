from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls import re_path
from django.views.static import serve

from where_to_go import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
