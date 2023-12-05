from django.urls import path, include
from rest_framework import routers
from tellevoapp.views import *
from tellevoapp.serializers import *

router = routers.DefaultRouter()
router.register('viaje', viajeViewSet)
router.register('usuario', userViewSet)
router.register('conductor', conductorViewSet)
router.register('vehiculo', vehiculoViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('', index, name=''),
    path('login/', custom_login, name='login'),
    path('api/get_user_data/', get_user_data, name='get_user_data'),
    path('vehiculos/usuario/<int:usuario_id>/', VehiculosUsuarioListView.as_view(), name='vehiculos-usuario-list'),
    path('index', index, name = 'index'),
]