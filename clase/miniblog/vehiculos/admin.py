from django.contrib import admin

from vehiculos.models import Marca, Vehiculos
# Register your models here.

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
        list_display = (
        'nombre',
    )

@admin.register(Marca)
class VehiculoAdmin(admin.ModelAdmin):
        list_display = (
        'marca', 'modelo',
    )
        