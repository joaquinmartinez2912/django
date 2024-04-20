from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from productos.models import Product, Category

# Para registrar y poder trabajar desde el administrador
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ("name", "price")
    search_fields = ["price","name","category__name"]
    list_filter = ["category"]
    #list_editable = ["price"]
    empty_value_display = "s/d"
    readonly_fields = ("name",)
    list_display_links = ("price","name")
    #exclude = ["description"]

    # list_display = ["__all__"] --> Ver como es el correcto para que funcione.
    list_display = ("name",
    "price",
    "rango_precios",
    "description",
    "category",
    #"stock",
    "get_stock",
    "valor_total")
    #date_hierarchy = "created"

    fieldsets = [
        (
            "info del Producto",
            {
                "fields" : ["name", "price"]
            }
        ),
        (
            "Info Extra",
            {
                "classes":["collapse"],
                "fields": ["stock", "description"]
            }
        )
    ]

    def valor_total(self, obj):
        return obj.stock * obj.price

    def get_stock(self, obj):
        codigo = "#FF0000"
        if obj.stock >= 500:
            codigo = "#008000"
        if 500 > obj.stock > 10:
            codigo = "#FFD300"
        return format_html(
            '<span style="color:{};">{}</span>',
            codigo, obj.stock
        )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


# class ProductAdmin(admin.ModelAdmin):
#      readonly_fields = ("created","modified")
# Despues habria que poner a esta clase como parametro  en fila 7