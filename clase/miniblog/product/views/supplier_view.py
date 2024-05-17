from django.shortcuts import render, redirect

from product.repositories.supplier import SupplierRepository
repo_sup = SupplierRepository()

def supplier_list(request):
    proveedores = repo_sup.get_all()
    return render(
        request,
        'supliers/list.html',
        dict(
            suppliers = proveedores
        )
    )

def suplier_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        proveedor_nuevo = repo_sup.create(
            nombre=name,
            direccion=address,
            telefono=phone,
        )
        return redirect('supplier_list')

    return render(
        request,
        'supliers/create.html',    
    )
