from rest_framework.response import Response
from rest_framework import serializers
from tellevoapp.models import * 

class ubicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'first_name', 'telefono']
        extra_kwargs = {'password': {'write_only': True}}

class ConductorFullSerializer(serializers.ModelSerializer):
    usuario = UserSerializer()

    class Meta:
        model = Conductor
        fields = ['id', 'nombre_usuario', 'numero_telefono', 'correo_electronico', 'viajes_realizados', 'usuario']

class ConductorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = ['id', 'nombre_usuario', 'numero_telefono', 'correo_electronico', 'viajes_realizados', 'usuario']

class vehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'