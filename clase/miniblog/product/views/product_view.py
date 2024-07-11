# Las vistas ejecutan un metodo que redireeciona a un template cuando se llama a una URL. 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from product.forms import ProductForm
from product.models import Category, ProductImage

from product.repositories.product import ProductRepository
from product.repositories.category import CategoryRepository

repo = ProductRepository()
repo_cat = CategoryRepository()

#TODO: Rearmar las vistas con formato de formulario.
class product_list(View):
    def get(self, request):
        productos = repo.get_all()
        return render(
            request,
            'products/list.html',
            dict(
                products=productos
            )
        )

class product_detail(View):
    def get(self, request, id):
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

class product_delete(View):
    def get(self, request, id):
        producto = repo.get_by_id(id=id) # No conviene hacer el .delete aca
        repo.delete(producto=producto)
        return redirect('product_list') # USamos el redirect para que nos lleve a la URL que en este caso es la misma

# @login_required(login_url="login")
class product_update(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, id):
        product = repo.get_by_id(id=id)

        initial_data = {
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category': product.category, 
            'stock': product.stock,
        }

        form = ProductForm(initial=initial_data)

        categorias = Category.objects.all()
        return render(
            request,
            'products/update.html',
            dict(
                form = form
                # categories = categorias,
                # product = product
            )
        )
    
    def post(self,request, id):
        form = ProductForm(request.POST)
        if form.is_valid():        
            producto_actualizado = repo.update(
                producto=repo.get_by_id(id=id),
                nombre=form.cleaned_data['name'],
                descripcion=form.cleaned_data['description'],
                precio=form.cleaned_data['price'],
                stock=form.cleaned_data['stock'],
                categoria=form.cleaned_data['category']
            )
            product=repo.get_by_id(id=id)
            prod = product.id
            print(prod)
            return redirect ('product_detail',prod )

class product_create(View):
    def get(self, request):
            form = ProductForm()
            
            # categorias = repo_cat.get_all()
            # Con el formulario no es necesario hacer esto de llamar las categorias con el repo.

            return render(
                request,
                'products/create.html',
                # Los nombres tienen que ser iguales que los que figuran en los templates
                dict(
                    # categories = categorias
                    form = form
                )
            )

    def post(self, request):
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


