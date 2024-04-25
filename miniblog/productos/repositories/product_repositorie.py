#import logging
from typing import (
    List,
    Optional
)

from productos.models import Product, Category
# Es la carpeta Productos

#logger = logging.getLogger(__name__)

class ProductRepository:
    # Metodo que trae todos los productos
    def get_all(self) -> List[Product]:
        return Product.objects.all()
    
    # Metodo para crear los product
    def create(
        self,
        nombre: str,
        precio:float,
        descripcion: Optional[str] = None,
        stocks: Optional[int] = None,
        categoria: Optional[Category] = None,
    )-> Product.objects:
        return Product.objects.create(
            name = nombre,
            price = precio,
            description = descripcion,
            stock = stocks,
            category = categoria,
        )
        
        # filtro_por_attr_1 = modelo.objects.filter(attr_1="valor")
    def filter_by_id(
            self,
            atributo:int,
    )   -> Optional[Product]:
        return Product.objects.filter(id=atributo).first()
    
    def get_by_id(self, id: int) -> Optional[Product]:
        try:
            product = Product.objects.get(id=id)
        except:
            product = None
        return product

    def get_product_on_price_range(
        self,
        min_price: float,
        max_price: float,
    ) -> List[Product]:
        #products = Product.objects.filter(
        #    price__gt=min_price,
        #    price__lt=max_price,
        #)
        products = Product.objects.filter(
            price__range=(min_price, max_price)
        )

        return products

    def filer_by_category_id(
            self,
            idCategory = int,
    ) -> Optional[Product]:
        categoria = Category.objects.filter(id=idCategory).first()
        if categoria is not None:
            return Product.objects.filter(category=categoria)
        return []    
    
    def filter_by_category_name(
        self,
        nombre_categoria: str,
    ) -> List[Product]:
        return Product.objects.filter(
            category__name=nombre_categoria
        )

    def filer_by_category(
            self,
            category = Category,
    ) -> Optional[Product]:
        return Product.objects.filter(category= category)

    def detele(self, producto: Product):
        return producto.delete()

    def get_product_gte_stock(
        self,
        cantidad_referencia = int,  
    ) -> Optional[Product]:
        return Product.objects.filter(stock__gt=cantidad_referencia)
    
    def get_product_lte_stock(
        self,
        cantidad_referencia = int,  
    ) -> Optional[Product]:
        return Product.objects.filter(stock__lt=cantidad_referencia) 