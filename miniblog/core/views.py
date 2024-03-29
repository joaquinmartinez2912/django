from django.http import HttpResponse

# Creo una vista
# index define el nombre de la ruta  --> Podria agregarlo directamente en las urls del proyecto, pero 
# optamos por definir un archivo urls en cada aplicacion
def index(request):
    return HttpResponse("Bienvenido a tercer año")

def about(request):
    return HttpResponse("Acerca de...")

