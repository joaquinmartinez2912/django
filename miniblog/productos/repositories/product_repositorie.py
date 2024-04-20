from typing import (
    List,
    Optional
)

from productos.models import Product, Category
# Es la carpeta Productos

class ProductRepository:
    # Metodo que trae todos los productos
    def get_all(self) -> List[Product]:
        return Product.objects.all()
    
    # Metodo para crear los product
    def create(
        self,
        nombre: str,
        descripcion: str,
        precio:float,
        stocks: int,
        categoria: Optional[Category] = None,
    )-> Product.objects:
        return Product.objects.create(
            name = nombre,
            description = descripcion,
            price = precio,
            category = categoria,
            stock = stocks,
        )
        
        # filtro_por_attr_1 = modelo.objects.filter(attr_1="valor")
    def filterById(
            self,
            atributo:int,
    )   -> Optional[Product]:
        return Product.objects.filter(id=atributo).first()
    
    def filerByCategoryId(
            self,
            idCategory = int,
    ) -> Optional[Product]:
        categoria = Category.objects.filter(id=idCategory).first()
        if categoria is not None:
            return Product.objects.filter(category=categoria)
        return []    
    
    def filerByCategoryId(
            self,
            category = Category,
    ) -> Optional[Product]:
        return Product.objects.filter(category= category)
    