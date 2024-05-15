from product.models import Category
from typing import List, Optional

class CategoryRepository:
    def get_all(self) -> List[Category]:
        return Category.objects.all()
    
    def create(
        self,
        nombre: str
    ) -> Category.objects:
        return Category.objects.create(
            name = nombre,
        )

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

    def update(self, 
        categoria:Category,
        nombre: str,
    ) -> Category :
        
        categoria.name = nombre

        categoria.save()

    def delete(
        self,
        categoria: Category
    ): return categoria.delete()