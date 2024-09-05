from django.db import models

class VehiculosQuerySet(models.QuerySet):
    def active(self):
        return self.filter(activo=True)
    
    def inactive(self):
        return self.filter(active=False)
    