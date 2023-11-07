from rest_framework.response import Response
from rest_framework import serializers
from tellevoapp.models import * 
from django.contrib.auth.models import User

class ubicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}