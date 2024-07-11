import csv

from vehiculos.models import Marca

from typing import Any
from typing import Any
from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    help = "Comando encargado de cargar marcas a partir de un CSV"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            'archivo_csv',
            type=str,
            help="Archivo csv desde donde se carga el modelo Marcas"
        )
    
    def handle(self, *args, **kwargs) -> str | None:
        csv_file = kwargs['archivo_csv']
        
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                nombre_marca = row['Marca']
                marca = Marca.objects.get_or_create(nombre=nombre_marca)
                self.stdout.write(self.style.SUCCESS(f"se cargo la marca {marca}"))
            self.stdout.write(self.style.WARNING(f"Finalizo la carga de la marca {marca}"))





