#Creado para mostrar las columnas que quieres mostrar en el endpoint
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer): #Devuelve todos los campos del modelo User
    class Meta:
        model = User
        fields = '__all__'

class UserClientSerializer(serializers.ModelSerializer): #Devuelve campos específicos del modelo User
    class Meta:
        model = User
        fields = [
            'name',
            'date_of_birth',
        ]
