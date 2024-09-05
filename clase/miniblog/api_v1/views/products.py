from rest_framework.viewsets import ModelViewSet
# from rest_framework import viewsets
from product.models import Product
from api_v1.serialezers.products_serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    


        
    