# Este archivo lo creo yo para que quede cada aplicacion con sus urls, no lo crea Django. Es convencion?

from django.urls import path

from core import views

# Todo archivo urls.py debe tener su patterns
# A su vez cada ruta que se cree, hay que agregarla en el patterns del proyecto
urlpatterns = [
    path('', views.index, name="index"),
    path("about/", views.about, name="about")
]
