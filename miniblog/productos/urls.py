
from django.urls import path

from productos import views

# Todo archivo urls.py debe tener su patterns
# A su vez cada ruta que se cree, hay que agregarla en el patterns del proyecto
urlpatterns = [
    path('roman', views.roman, name="roman"),
    #path("about/", views.about, name="about")
]
