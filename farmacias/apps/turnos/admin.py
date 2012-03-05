from django.contrib import admin

from apps.turnos.models import Farmacia
from apps.turnos.models import Turno

class FarmaciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'lat', 'lon', 'revisado')
    search_fields = ['nombre', 'direccion']
    class Meta:
        model = Farmacia

admin.site.register(Farmacia, FarmaciaAdmin)
admin.site.register(Turno)

