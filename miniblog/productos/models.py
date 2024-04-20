from django.contrib import admin
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        null=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete = models.SET_NULL,
        related_name="products",
        null=True, blank=True
    )
    stock = models.IntegerField(
        default=0
    )

    #created = models.DateTimeField(auto_now_add=True)
    #modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self) -> str:
        return self.name
    
    @admin.display(description="Rango de precio")
    def rango_precios(self):
        if self.price > 40000:
            return "Alto"
        if 20000 < self.price < 400000:
            return "Medio"
        return "Bajo"
    
    # def save(self, *args, **kwargs):
    #     if self.price>0:
    #         super().save()
    #     else:
    #         print("Error")