from django.db import models
from datetime import datetime

from vehiculos.managers import VehiculosQuerySet
# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre
    

class Vehiculos(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    fabricado_el = models.IntegerField(default=datetime.now().year)
    cantidad_puertas = models.IntegerField()
    cilindrada = models.FloatField()
    tipo_combustible = models.CharField(max_length=50)
    preio_dolares = models.IntegerField()
    activo = models.BooleanField(default=True)

    objects = VehiculosQuerySet.as_manager()

    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} {self.fabricado_el}"
    
    