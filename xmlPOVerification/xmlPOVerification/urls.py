import verificacao.views as views
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', admin.site.urls),
    url(r'^$', views.button),
    url(r'^output', views.output, name="script"),
]

# Alterar a interface do Django Admin:
admin.site.site_header = 'Supply | PetLove'
admin.site.index_title = 'Verificação das Notas'
admin.site.site_title = 'SUPPLY - PetLove'
