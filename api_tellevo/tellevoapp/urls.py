from django.urls import path, include
from rest_framework import routers
from tellevoapp.views import *
from tellevoapp.serializers import *

router = routers.DefaultRouter()
router.register('ubicacion', ubicacionViewSet)
router.register('usuario', userViewSet)

urlpatterns = [
    path('', include(router.urls)),
]