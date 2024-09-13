import django_filters

from product.models import Product

# Formato para hacer la consulta en la URL = http://127.0.0.1:8000/api_v1/products/?category=Utensillos
class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(
        field_name='category__name',
        lookup_expr='icontains'
        )
    
    class Meta:
        model = Product
        fields = ['category',]


