from django.shortcuts import render
from django.http import HttpResponse

from productos.repositories.product_repositorie import ProductRepository
# from .models import Product
# Create your views here.

repo = ProductRepository()

def product_list(request):
    productos = repo.get_all()
    return render(
        request,
        'products/list.html',
        dict(
            products=productos
        )
    )
    
def product_detail(request,id):
    producto = repo.get_by_id(id=id)
    return render(
        request,
        'products/detail.html',
        {"product":producto}
    )

def product_delete(request,id):
    ...

def product_update(request,id):
    ...

def product_create(request):
    ...




# def roman(request):
#     productos = Product.objects.all()
#     contenido_html = "<ul>"
#     for producto in productos:
#         contenido_html += f"<li>{producto.name}</li>"
#     contenido_html += "</ul>"
#     return HttpResponse(contenido_html)