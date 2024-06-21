# Las vistas ejecutan un metodo que redireeciona a un template cuando se llama a una URL. 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from product.forms import ProductForm
from product.models import Category, ProductImage

from product.repositories.product import ProductRepository
from product.repositories.category import CategoryRepository

repo = ProductRepository()
repo_cat = CategoryRepository()

#TODO: Rearmar las vistas con formato de formulario.
def product_list(request):
    productos = repo.get_all()
    return render(
        request,
        'products/list.html',
        dict(
            products=productos
        )
    )

def product_detail(request, id):
    producto = repo.get_by_id(id=id)

    imagen = ProductImage.objects.filter(product=producto).first()
    return render(
        request,
        'products/detail.html',
        {
            "product":producto,
            "imagen": imagen
        }
    )

def product_delete(request, id):
    producto = repo.get_by_id(id=id) # No conviene hacer el .delete aca
    repo.delete(producto=producto)
    return redirect('product_list') # USamos el redirect para que nos lleve a la URL que en este caso es la misma

@login_required(login_url="login")
def product_update(request, id):
    product = repo.get_by_id(id=id)
    print(product.name)
    categorias = Category.objects.all()
    if request.method == "POST":
        product = repo.get_by_id(id=id) # Como sabe que el id es el de la URL?
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        id_category = request.POST.get('id_category')
        category = Category.objects.get(id=id_category)
    
        repo.update(
            producto=product,
            nombre=name,
            precio=float(price),
            descripcion=description,
            stock=stock,
            categoria=category
        )
        
        return redirect('product_detail', product.id)

    return render(
        request,
        'products/update.html',
        dict(
            categories = categorias,
            product = product
        )
    )

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            producto_nuevo = repo.create(
                nombre=form.cleaned_data['name'],
                descripcion=form.cleaned_data['description'],
                precio=form.cleaned_data['price'],
                cantidades=form.cleaned_data['stock'],
                categoria=form.cleaned_data['category']
            )
            return redirect ('product_list')

        # Esta parte la saco porque ahora instancio el producto con el formulario
        # name = request.POST.get('name')
        # description = request.POST.get('description')
        # price = request.POST.get('price')
        # stock = request.POST.get('stock')
        # id_category = request.POST.get('id_category') # Porque es el nombre que pusimos en el formulario
        # category = Category.objects.get(id=id_category)

        # producto_nuevo = repo.create(
        #     nombre=name,
        #     descripcion=description,
        #     precio=float(price),
        #     cantidades=stock,
        #     categoria=category
        # )
        # return redirect('product_detail', producto_nuevo.id)

        
    categorias = repo_cat.get_all()
    # Con el formulario no es necesario hacer esto de llamar las categorias con el repo.
    form = ProductForm()

    return render(
        request,
        'products/create.html',
        # Los nombres tienen que ser iguales que los que figuran en los templates
        dict(
            # categories = categorias
            form = form
        )
    )

