from rest_framework.viewsets import ModelViewSet
# from rest_framework import viewsets
from product.models import Product, Category
from rest_framework  import status
from api_v1.serialezers.products_serializers import ProductSerializer
from api_v1.paginations import MiPaginador
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from api_v1.filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # pagination_class = MiPaginador
    filter_backends = [SearchFilter, DjangoFilterBackend ]
    # search_fields = ['name' ]
    # filterset_class = ProductFilter
    search_fields = ['name', 'stock', 'category__name']
    filterset_class = ProductFilter

    # Filtros personalizados:
    # def get_queryset(self):
    #     # queryset = self.queryset.filter(active=True) TODO: Tengo que hacer el campo active
    #     queryset = super().get_queryset() 
    #     category = self.request.query_params.get('category')
    #     min_price = self.request.query_params.get('min_price')
    #     max_price = self.request.query_params.get('max_price')
    #     if min_price:
    #         queryset = queryset.filter(price__gte=min_price)
    #     if max_price:
    #         queryset = queryset.filter(price__lte=max_price)
    #     if category:
    #         queryset = queryset.filter(category__name=category)
    #     return queryset

    def create(self, request, *args, **kwargs):

        # El request data es el formulario que viene del front
        data = request.data

        category_data = data.get('category')
        # category_name = data.get('name') FIXME: Ver en el repo que hace aca
        category, created = Category.objects.get_or_create(
            name=category_data.get('name')
        )

        #Creamos el producto:
        product = Product.objects.create(
            name=data.get['name'],
            description=data.get['description'],
            price=data.get['price'],
            stock=data.get['stock'],
            category=category,
        )
        #Aca hay que serilizarlo, a diferencia de si lo hubiamos armado en "products_serializer"
        serialezer = self.serializer_class(product)
        return Response(serialezer.data, status=status.HTTP_201_CREATED)

    # Este no se puede hacer desde el lado del serialezer.
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
