from django.contrib import admin
from .models import Verificação 

@admin.register(Verificação)
class Verificação(admin.ModelAdmin):
    def response_change(self, request, obj):
        if "_verificar" in request.POST:
            self.message_user(request, "Teste de Verificação XML")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)
