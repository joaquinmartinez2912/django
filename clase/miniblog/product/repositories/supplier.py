from product.models import Supplier
from typing import List, Optional

class SupplierRepository:
    def get_all(self) -> List[Supplier]:
        return Supplier.objects.all()
    
    def create(
        self,
        nombre: str,
        direccion = str,
        telefono = str,
    ) -> Supplier.objects:
        return Supplier.objects.create(
            name=nombre,
            address=direccion,
            phone=telefono,
        )

    def filter_by_id(
        self,
        id_atributo = int
    ) -> List[Supplier]:
        return Supplier.objects.filter(
            id = id_atributo
        )
    
    def get_by_id(self, id: int) -> Optional[Supplier]:
        try:
            supplier = Supplier.objects.get(id=id)
        except:
            supplier = None
        return supplier 

    def update(self, 
        proveedor:Supplier,
        nombre: str,
        direccion = str,
        telefono = str,
    ) -> Supplier :
        
        proveedor.name = nombre
        proveedor.address = direccion
        proveedor.phone = telefono

        proveedor.save()

    def delete(
        self,
        proveedor: Supplier
    ): return proveedor.delete()