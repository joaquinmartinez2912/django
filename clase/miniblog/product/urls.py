from django.urls import path

from product.views.product_view import (
    product_list,
    product_create,
    product_delete,
    product_detail,
    product_update,
)

from product.views.category_view import ( 
    category_list, 
    category_create, 
    category_delete,
    category_update,
    category_detail,
    )

from product.views.supplier_view import (
    supplier_list,
    suplier_create,
    suplier_delete,
    suplier_update,
    suplier_detail,
)

from product.views.product_review_view import (
    ProductReviewView,
    ProductReviewCreateView,
    ProductREviewDetailView,
    ProductREviewUpdateView,
)

from product.views.product_image_view import (
    ProductImageView
)

urlpatterns = [
    path(route='', view=product_list.as_view(), name='product_list'),
    path(route='create/',view=product_create.as_view(), name='product_create'),
    path(route='<int:id>/',view=product_detail.as_view(),name="product_detail"),
    path(route='<int:id>/update/',view=product_update.as_view(),name="product_update"),
    path(route='<int:id>/delete/',view=product_delete.as_view(),name="product_delete"),
    path(route='category',view=category_list,name="category_list"),
    path(route='category/<int:id>/delete/',view=category_delete,name="category_delete"),
    path(route='category/create',view=category_create, name='category_create'),
    path(route='category/<int:id>/update/',view=category_update,name="category_update"),
    path(route='category/<int:id>/detail/',view=category_detail,name="category_detail"),
    path(route='supplier',view=supplier_list,name="supplier_list"),
    path(route='supplier/create',view=suplier_create, name='suplier_create'),
    path(route='supplier/<int:id>/delete/',view=suplier_delete, name='suplier_delete'),
    path(route='supplier/<int:id>/update/',view=suplier_update, name='suplier_update'),
    path(route='supplier/<int:id>/detail/',view=suplier_detail, name='suplier_detail'),
    path(route='product_reviews/',view=ProductReviewView.as_view(),name="product_reviews"),
    path(
        route='product_reviews/create',
        view=ProductReviewCreateView.as_view(),
        name="product_reviews_create"),
    path(
        route='product_reviews/<int:id>',
        view=ProductREviewDetailView.as_view(),
        name="product_reviews_detail"),
    path(
        route='product_reviews/<int:id>/update',
        view=ProductREviewUpdateView.as_view(),
        name="product_reviews_update"),
    path(route='product_images/',
         view=ProductImageView.as_view(),
         name="product_images"),
]


