from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import viewsets
from tellevoapp.models import *
from tellevoapp.serializers import * 
from django.contrib.auth.models import User

# Create your views here.
class ubicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = ubicacionSerializer
    
class userViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class conductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ConductorPostSerializer
        return ConductorFullSerializer

class vehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = vehiculoSerializer
    