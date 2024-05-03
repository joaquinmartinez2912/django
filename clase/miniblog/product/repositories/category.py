from product.models import Category
from typing import List

class CategoryRepository:
    def get_all(self) -> List[Category]:
        return Category.objects.all()