from django.db import models
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


class CustomUser(AbstractUser):
    telefono = models.IntegerField(blank=True, null=True)
    def save(self, *args, **kwargs):
        # Cifrar la contraseña si se proporciona una
        if self.password:
            self.set_password(self.password)
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username
    
class Conductor(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    nombre_usuario = models.CharField(max_length=255, null=False)
    numero_telefono = models.IntegerField(null=False)
    correo_electronico = models.CharField(max_length=255, null=False)
    viajes_realizados = models.IntegerField(null=False)
    nombre_completo = models.CharField(max_length=255, null=False)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.nombre_usuario

class Viaje(models.Model):
    inicio_lat = models.DecimalField(max_digits=10, decimal_places=10)
    inicio_lon = models.DecimalField(max_digits=10, decimal_places=10)
    destino_lat = models.DecimalField(max_digits=10, decimal_places=10)
    destino_lon = models.DecimalField(max_digits=10, decimal_places=10)
    tarifa = models.IntegerField(null=False)
    metodo_pago = models.CharField(max_length=255, null=False)
    usuario_viaje = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.inicio_viaje
    
class Vehiculo(models.Model):
    patente = models.CharField(max_length=255, null=False)
    marca = models.CharField(max_length=255, null=False)
    modelo = models.CharField(max_length=255, null=False)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.patente





