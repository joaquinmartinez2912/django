from product.models import Product, Category
from django.core.cache import cache


# def all_names_product(request):
#     products = Product.objects.all()
#     names = [product.name for product in products]
#     return dict(
#         names=names
#     )

# Con cache.
def all_names_product(request):
    products = cache.get('products')
    if products is None:
        products = Product.objects.all().values_list('name')
        cache.set('products', products, 36000)
    return dict(
        names=products
    )

def all_names_category(request):
    categories = Category.objects.all()
    names = [category.name for category in categories]
    return dict(
        names_category=names
    )


 