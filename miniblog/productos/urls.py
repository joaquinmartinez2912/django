
from django.urls import path

from productos.views import (
    product_list,
    product_create,
    product_detail,
    product_delete,
    product_update
)

# Todo archivo urls.py debe tener su patterns
# A su vez cada ruta que se cree, hay que agregarla en el patterns del proyecto
urlpatterns = [
    path(route="",view=product_list, name='product_list'),
    path(route="create/",view=product_create, name='product_create'),
    path(route="<int:id>/",view=product_detail, name='product_detail'),
    path(route="<int:id>/update/",view=product_update, name='product_update'),
    path(route="<int:id>/delete",view=product_delete, name='product_delete'),
    # path('roman', views.roman, name="roman"),
    #path("about/", views.about, name="about")
]
