from django.db import models
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    telefono = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.username

class Ubicacion(models.Model):
    inicio_viaje = models.CharField(max_length=255, null=False)
    destino_viaje = models.CharField(max_length=255, null=False)
    tarifa = models.IntegerField(null=False)
    
    def __str__(self):
        return self.nombre_ubicacion
    
class Vehiculo(models.Model):
    patente = models.CharField(max_length=255, null=False)
    marca = models.CharField(max_length=255, null=False)
    modelo = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.patente

class Conductor(models.Model):
    nombre_usuario = models.CharField(max_length=255, null=False)
    numero_telefono = models.IntegerField(null=False)
    correo_electronico = models.CharField(max_length=255, null=False)
    viajes_realizados = models.IntegerField(null=False)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_usuario



