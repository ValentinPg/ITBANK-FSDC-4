
from urllib import request
from django.db import models

from clientes.models import User


class SolicitudesPrestamos(models.Model):
    
    id_solicitud = models.AutoField(primary_key=True)
    monto = models.CharField(max_length=100,verbose_name="monto")
    fecha_inicio =  models.DateField(verbose_name="fecha de inicio")
    tipo_prestamo = models.CharField(max_length=100,default="tipo_prestamo", verbose_name="tipo de prestamo")
    
    fecha_solicitud = models.DateTimeField(auto_now_add=True, null=True, verbose_name="fecha de creación")
    fecha_modificacion = models.DateTimeField(auto_now_add=True, null=True, verbose_name="fecha de modificación")
    
    
    usuario = models.IntegerField()
    