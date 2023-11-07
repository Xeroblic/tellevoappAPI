from django.db import models

# Create your models here.
class Ubicacion(models.Model):
    nombre_ubicacion = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.nombre_ubicacion