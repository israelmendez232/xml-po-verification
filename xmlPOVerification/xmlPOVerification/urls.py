from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Alterar a interface do Django Admin:
admin.site.site_header = 'Supply | PetLove'
admin.site.index_title = 'Verificação das Notas'
admin.site.site_title = 'SUPPLY - PetLove'
