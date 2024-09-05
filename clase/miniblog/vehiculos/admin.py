from django.contrib import admin

from vehiculos.models import Marca, Vehiculos
# Register your models here.

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
        list_display = (
        'nombre',
    )

@admin.register(Vehiculos)
class VehiculoAdmin(admin.ModelAdmin):
        list_display = (
        'marca', 'modelo',
    )
        