from django.contrib import admin
from core.models import Guarderias, Reserva

# Register your models here.

class guarderiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'codigo')
    search_fields=['nombre'] #SE pasa tupla. no lista para buscar
    readonly_fields=('created','updated') ##Archivos que no se pueden editar
    filter_horizontal=()
    list_filter=()
    fieldsets=()


admin.site.register(Guarderias, guarderiaAdmin) ##Se le pasa la funcion del modelo creada(guarderias)


##@admin.register(Reserva)
class reservaAdmin(admin.ModelAdmin):
    list_display = ('guarderia', 'f_inicio', 'f_fin')
    list_filter = ('guarderia', 'f_inicio', 'f_fin')
    search_fields=('guarderia__codigo',) #SE pasa tupla. no lista para buscar


admin.site.register(Reserva, reservaAdmin) ##Se le pasa la funcion del modelo creada(guarderias)