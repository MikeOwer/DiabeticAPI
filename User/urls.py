# Fue creado para los endpoints de la app de User
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users',UserViewSet) #Registro de la vista de User

urlpatterns = [
    path('',include(router.urls)),
]