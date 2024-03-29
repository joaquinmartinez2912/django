from django.contrib import admin

# Register your models here.
from productos.models import Product

# Para registrar y poder trabajar desde el administrador
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description")
