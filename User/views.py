from django.shortcuts import render
from rest_framework import viewsets, status
from .models import User # . es para el nombre del archivo
from .serializers import UserSerializer,UserClientSerializer
from rest_framework.decorators import action 
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() #Se obtienen todos los usuarios
    serializer_class = UserSerializer #Se utiliza el serializer general para traer todos los campos

    
    @action(detail=False,methods=['get'])
    def user_client(self,request):
        queryset = self.get_queryset() #Se está utilizando el queryset de la misma view (Clase)
        serializer = UserClientSerializer(queryset,many=True) #Se utiliza el serializer personalizado 
        return Response(serializer.data)
    
    @action(detail=False, methods=['post']) #No funciona 
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        print(email)
        print(password)

        # Autenticar al usuario
        user = authenticate(email=email, password=password)
        print(user)

        if user is not None:
            # Si las credenciales son válidas, devolver la información del usuario
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        else:
            # Si las credenciales no son válidas, devolver un error
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_400_BAD_REQUEST)

''' 
    def user_view(request):
        queryset = User.objects.all()
        filter = UserFilter(request.GET, queryset=queryset)
        filtered_users = filter.qs.values('name', 'date_of_birth')
        
        return Response(filtered_users)
'''
