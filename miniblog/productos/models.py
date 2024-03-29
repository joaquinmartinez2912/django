from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #created = models.DateTimeField(auto_now_add=True)
    #modified = models.DateTimeField(auto_now=True)

    # class Meta:
    #     verbose_name = "Producto"
    #     verbose_name_plural = "Productos"

    def __str__(self) -> str:
        return self.name
    
    
    # def save(self, *args, **kwargs):
    #     if self.price>0:
    #         super().save()
    #     else:
    #         print("Error")