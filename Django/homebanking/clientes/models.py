from random import randrange
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    tipoid = models.IntegerField(db_column='tipoId', blank="True", null="True")

    class Meta:
        managed = False
        db_table = 'cliente'
        
        
class TiposCliente(models.Model):
    tipoid = models.AutoField(db_column='tipoId', primary_key=True)  # Field name made lowercase.
    plan_cliente = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipos_cliente'
        

        
class Direccion(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=255, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=255, blank=True, null=True)
    customer_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    employee_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    branch_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'

class User(AbstractUser):
    customer = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=randrange(1,505)) #esta puesto para que gener un numero random como prueba, la idea es que cuando el usuario se registre o cuanda vaya a autenticarse ingrese su numero de cliente y este es unico.