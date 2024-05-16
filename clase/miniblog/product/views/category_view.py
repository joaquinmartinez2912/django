from django.shortcuts import render, redirect

from product.repositories.category import CategoryRepository
repo_cat = CategoryRepository()

from product.repositories.product import ProductRepository
repo_prod = ProductRepository()

def category_list(request):
    category_repository = CategoryRepository()
    categorias = category_repository.get_all()
    return render(
        request,
        'categories/list.html',
        dict(
            categories = categorias
        )
    )

def category_detail(request, id):
    categoria = repo_cat.get_by_id(id=id)
    productos = repo_prod.filter_by_category(categoria)
    return render(
        request,
        'categories/detail.html',
        dict(
            category = categoria,
            products = productos
        )
    )

def category_update(request, id):
    category = repo_cat.get_by_id(id=id)

    if request.method == "POST":
        category = repo_cat.get_by_id(id=id) # Como sabe que el id es el de la URL?
        name = request.POST.get('name')

        repo_cat.update(
            categoria=category,
            nombre=name,
        )
        
        return redirect('category_list')

    return render(
        request,
        'categories/update.html',
       
        dict(
             categoria = category,
        )
       
    )

def category_delete(request, id):
    categoria = repo_cat.get_by_id(id=id) # No conviene hacer el .delete aca
    repo_cat.delete(categoria=categoria)
    return redirect('category_list')

def category_create(request):
    if request.method == "POST":
        name = request.POST.get('name')

        categoria_nuevo = repo_cat.create(
            nombre=name,
        )
        return redirect('category_list')

    return render(
        request,
        'categories/create.html',    
    )


