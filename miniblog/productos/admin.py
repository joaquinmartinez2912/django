from django.contrib import admin

# Register your models here.
from productos.models import Product, Category

# Para registrar y poder trabajar desde el administrador
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ("name", "price")
    search_fields = ["price","name","category__name"]
    list_filter = ["category"]
    list_editable = ["price"]
    empty_value_display = "s/d"
    exclude = ["description"]

    # list_display = ["__all__"] --> Ver como es el correcto para que funcione.
    list_display = ("name", "price", "description","category")
    #date_hierarchy = "created"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


# class ProductAdmin(admin.ModelAdmin):
#      readonly_fields = ("created","modified")
# Despues habria que poner a esta clase como parametro  en fila 7