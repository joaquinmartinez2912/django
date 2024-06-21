# Clase Django.
Trabajo de clases - Django 2024.
## Tabla de contenidos
- [Entorno Virtual e Inicio Local](#entorno-Virtual-e-Inicio-Local)

- [Comandos Utiles](#comandos-utiles)

- [ORM](#orm)


## *Entorno Virtual e Inicio Local*
***
**Paso 1.**

Crear entorno virtual de python:

* Linux

```
python3 -m venv venv
```
* Windows con versiones de python menores a 3.10. Luego de descargar la version hago

```
 "C:\Users\Joaquin\AppData\Local\Programs\Python\Python310\python.exe" -m venv 
 ```
Es la ubicacion segun donde se haya guardado la version.

**Paso 2.**

Activar entorno virtual.

* Linux
```
source venv/bin/activate
```
source .venv/Scripts/activate

* Windows
```
source .venv/Scripts/activate
```


**Paso 3.**

Instalar Django

* Linux
```
pip install django
```




**Para levantar.**

Dentro del entorno, levantar el archivo requirements.txt que contiene las dependencias necesarias para poder trabajar.

```
pip install -r requirements.txt
```

Para actualizar dependecias
```
pip freeze>requirements.txt
```

## *Comandos utiles*

**Crear un proyecto nuevo**
```
django-admin startproject (nombre)
```

Directorios del proyecto
wsgi: Es donde se corre efectivamente el proyecto
urls: rutas del proyecto, que son distintas que las rutas de la aplicacion.
settings:  Puede crearse uno distinto por cada ambiente.

DEBUG: TRUE o FALSE si esta en preoduccion.

INSTALED_APPS: Aca voy agregando las aplicaciones que  que creo.

DATABASES: De Momento usamos SQLITE 

LANGUAGE_CODE = "es"
TIME_ZONE = 

manage.py: Corre los comandos de Django. Los podemos crear y correrlos a partir de aca.

**Correr el proyecto (Primero me muevo a la carpeta donde esta el proyecto)**
```
python3 manage.py runserver
```
Puerto en que corre: 8000

**Crear una aplicacion**
```
python3 manage.py startapp (nombre)
```
Se genere un nuevo directorio con:
 - migraciones
 - models: Aca se generan los modelos para crear las tablas de bases de datos 
 - views: Crea las vistas

 **Crear un usuario de aministrador**
 Primero tengo que tener en cuenta de que esten listas las migraciones que viene predefinidas
```
python3 manage.py createsuperuser --username (nombre)
```

 **Hacer migraciones de las app preestablecidas**

 Para verlo en DB Beaver, primero creo una conexion SQLite levantando el archivo del tipo
 y despues
```
python3 manage.py migrate
```
 **Hacer migraciones de los modelos que creo en las aplicaciones**
Tengo que chequear primero que la aplicacion este establecida como parte del proyecto. Se hace desde
Settings, INSTALED APPS
```
python3 manage.py makemigrations
```
Despues de esto, para que se vea tengo que hacer:

```
python3 manage.py migrate
```

## *ORM*

 **Abri Shell (Consola)**
```
python3 manage.py shell
```

 **Instalar consola ipython**
Es otro tipo de consola
```
pip install ipython
```
Una vez instalada se abre con el comando anterior, sola que sino la instalas te tira la predeterminada.

### DENTRO DE LA SHELL:  

**PARA TRAER LA BASE**
```
from productos.models import Product
```

**PARA OBTENER UN LISTADO DE PRODCUTOS**
```
NombreModelo.objects.all()
Product
```
**NUEVO PRODUCTO**
```
 nuevo_producto = Product.objects.create(
   ...: name="microfono",
   ...: description="Con condensador",
   ...: price=float(15000),
   ...: )
```

**PARA SELECCIONAR UNO:**
```
NombreModelo.objects.first()
Product
```

**PARA ACCEDER A LO ULTIMO QUE VI:**
```
producto_2=_
```

**PARA ACCEDER A UN ATRIBUTO:**
```
producto_2.name
```
**PARA MODIFICAR**
```
producto_2.name = (nuevo nombre)_
```
para que actualice hay que hacer:
```
producto_2.save()
```
**PARA BORRARLO**
```
producto_2.delete
```

**PARA FILTRAR POR ATRIBUTO 1:**
```
filtro_por_attr_1 = modelo.objects.filter(attr_1="valor")
```
Devuelve un queryset que no admite una consulto por atributo ya que el filter trae una lista y 
no un objeto determinado. El get lo usamos cuando sabemos que el elemento en particular existe.

**PARA AGREGAR MAS DE UN FILTRO:**
```
producto_por_id = products.objects.filter(id=1,price=float(30000))
```
**PARA ORDENAR:**
```
Product.objects.all().order_by("price")
```

**EXCLUIR ELEMENTOS:**
```
Modelo.objects.exclude(attr_2="value")
```

**GUARDAR ULTIMA SALIDA:**
```
productos = _
```

**CONSULTAR TODOS LOS REGISTROS**
```
modelo = Modelo.objects.all()
```

**ACCEDER AL PRIMER ELEMENTO**
```
modelo = Modelo.objects.first()
```

**ACCEDER AL ULTIMO ELEMENTO**
```
modelo = Modelo.objects.last()
```

**CONTAR CANTIDAD DE ELEMENTOS DE UN QUERYSET**
```
cantidad_de_elementos = len(modelo)
```

**CONTAR ELEMENTOS**
```
cantidad_de_elementos = Modelo.objects.count()
```

**ORDENERLOS**
```
Modelo.objects.all().order_by('attr')
```

**EXCLUIR ELEMENTOS**
```
Modelo.objects.exclude('attr_2'='value')
```

**LOOKUP IXECT/EXCT**
```
Modelo.objects.filter(attr_1__iexact='Value') # No distingue mayusculas o minisculas
```
```
Modelo.objects.filter(attr_1__exact='Value') # Distingue mayusculas y minusculas
```
**MAYOR Y MENOR**
```
Modelo.objects.filter(attr_1__gt=50)
```
```
Modelo.objects.filter(attr_1__lt=50)
```

**IN LISTA**
```
Modelo.objects.filter(attr_2__in=['value', 'value'])
```

**COMIENZO DE VALOR DE ATRIBUTO**
```
Modelo.objects.filter(attr__startswith='Va')
```

**FINAL DE ATRIBUTO**
```
Modelo.objects.filter(attr__endswith='Va')
```

**FILTRADO POR RANGO**
```
Modelo.objects.filter(attr_1__range=(valor2, valor2)
```

**For para crear objetos en shell*

creo una lista con nombres y una con adjtivos e importo "radmon" y luego:

```
from productos.models import Category, Product

nombres = ["mouse","teclado","notebook","impresora","teclas","router","m
   odem", "procesador","placa madre","cooler","transformador","scanner","mu
   ltifuncion"]

adj = ["mod18","mod19","mod20","mod21","mod22","mod23","mod24"]

import random

for i in range (15):
     nuevo_producto = Product.objects.create(
     name = f"{random.choice(nombres)} {random.choice(adj)}",
     description = "",
     price = random.randint(10000,80000),
     category = Category.objects.first(),
     )
```

Comando para que se reinicie la Shell cuando hay un cambio. Se debe hacer primero que todo.
```
%load_ext autoreload

%autoreload 2
```

In [4]: from productos.repositories.product_repositorie import ProductRepository
   ...: 

In [5]: repository = ProductRepository()

In [6]: repository.get_all()
Out[6]: <QuerySet [<Product: microfono>, <Product: Monitor>, <Product: notebook>, <Product: scanner>, <Product: modem>, <Product: modem>, <Product: multifuncion mod19>, <Product: procesador mod24>, <Product: modem mod18>, <Product: scanner mod20>, <Product: impresora mod20>, <Product: router mod18>, <Product: teclas mod21>, <Product: scanner mod24>, <Product: router mod23>, <Product: teclado mod19>, <Product: procesador mod24>, <Product: scanner mod24>, <Product: multifuncion mod24>, <Product: impresora mod19>, '...(remaining elements truncated)...']>

```
nuevo_producto = repository.create("casco","casquito",6000,70)
```