from django.shortcuts import render
from django.http import HttpResponse



from .models import Product
# Create your views here.

def roman(request):
    productos = Product.objects.all()
    contenido_html = "<ul>"
    for producto in productos:
        contenido_html += f"<li>{producto.name}</li>"
    contenido_html += "</ul>"
    return HttpResponse(contenido_html)