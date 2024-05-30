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

def suplier_delete(request, id):
    proveedor = repo_sup.get_by_id(id=id) # No conviene hacer el .delete aca
    repo_sup.delete(proveedor=proveedor)
    return redirect('supplier_list') 

def suplier_update(request, id):
    suplier = repo_sup.get_by_id(id=id)
    if request.method == "POST":
        proveedor = repo_sup.get_by_id(id=id) # Como sabe que el id es el de la URL?
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

    
        repo_sup.update(
            proveedor=proveedor,
            nombre=str(name),
            direccion=str(address),
            telefono=str(phone),
        )
        
        return redirect('supplier_list')

    return render(
        request,
        'supliers/update.html',
        dict(
            suplier = suplier,
        )
    )

def suplier_detail(request, id):
    proveedor = repo_sup.get_by_id(id=id)
    return render(
        request,
        'supliers/detail.html',
        {"suplier":proveedor}
    )
