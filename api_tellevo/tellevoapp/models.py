from django.db import models

# Create your models here.
class Ubicacion(models.Model):
    nombre_ubicacion = models.CharField(max_length=255, null=True)