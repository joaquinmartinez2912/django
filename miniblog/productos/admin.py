from django.contrib import admin

# Register your models here.
from productos.models import Product

# Para registrar y poder trabajar desde el administrador
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description")
    #date_hierarchy = "created"


# class ProductAdmin(admin.ModelAdmin):
#      readonly_fields = ("created","modified")
# Despues habria que poner a esta clase como parametro  en fila 7