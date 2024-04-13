from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    #url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    path('', include("main.urls")),
    path('admin/', admin.site.urls),
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
