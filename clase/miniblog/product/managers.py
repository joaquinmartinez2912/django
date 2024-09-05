from django.db import models

# De models.queryset todos los que devuelven un queryset
class ProductQuerySet(models.QuerySet):
    def get_informatica(self):
        return self.filter(category__name="Info")
    
# De models.manager todos los que devuelven un resultado.
class ProductManager(models.Manager):
    def total_price(self):
        priceTotal = 0
        for product in self:
            priceTotal += product.price
        return priceTotal

