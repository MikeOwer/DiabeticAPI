from django.db import models
from paranoid_model.models import Paranoid as pan
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
#Se utilizó django paranoid model


class CustomUserManager(BaseUserManager): #Para crear un superuser. No sirve actualmente.
    def create_user(self, email, password=None,**extra_fields):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(pan,AbstractBaseUser): #Modelo de usuario
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255,null=True)
    date_of_birth = models.DateField()
    last_login = models.DateField(blank=True,null=True)

    objects = CustomUserManager() #Verificar este funcionamiento.

    USERNAME_FIELD = 'email' #Necesario para autenticación
    REQUIRED_FIELDS = ['name','last_name'] #Necesario para autenticación



class Record(pan):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    urls_info = models.JSONField()
    in_level_3 = models.BooleanField()
    last_level_2 = models.DateField()
    last_level_3 = models.DateField()

class Activity(pan):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_level = models.IntegerField()
    current_question = models.IntegerField()
    questions_answered = models.IntegerField()
    last_date = models.DateField()
    times_in = models.IntegerField()

class MedicalHistory(pan):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    glucose = models.DecimalField(max_digits=20,decimal_places=3)
    systolic_pressure = models.DecimalField(max_digits=20,decimal_places=3)
    diastolic_pressure = models.DecimalField(max_digits=20,decimal_places=3)
    glucosylated_hemoglobin_a1c = models.DecimalField(max_digits=20,decimal_places=3)

