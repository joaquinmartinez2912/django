from typing import(
    List,
    Optional
)

from productos.models import Product, Category

class CategoryRepository:

    def create(
        self,
        nombre: str
    ) -> Category.objects:
        return Category.objects.create(
            name = nombre,
        )
        
    def get_all(
        self
    ) -> List[Category]:
        return Category.objects.all()
    
    def filter_by_id(
        self,
        id_atributo = int
    ) -> List[Category]:
        return Category.objects.filter(
            id = id_atributo
        )
    
    def get_by_id(self, id: int) -> Optional[Category]:
        try:
            category = Category.objects.get(id=id)
        except:
            category = None
        return category