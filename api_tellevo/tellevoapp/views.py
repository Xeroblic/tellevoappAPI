from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import viewsets
from tellevoapp.models import *
from tellevoapp.serializers import * 
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login


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
    
@csrf_exempt
@require_POST
def custom_login(request):
    # Recuperar las credenciales del cuerpo de la solicitud POST
    username = request.POST.get('username')
    password = request.POST.get('password')

    # Autenticar al usuario
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # Iniciar sesión para persistir la autenticación en la sesión
        login(request, user)
        return JsonResponse({'detail': 'Login exitoso'})
    else:
        return JsonResponse({'detail': 'Error en las credenciales'}, status=401)
    