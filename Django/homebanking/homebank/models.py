from django.db import models


class SolicitudesPrestamos(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    monto = models.CharField(max_length=100,verbose_name="monto")
    fecha_inicio =  models.DateField(verbose_name="fecha de inicio")
    tipo_prestamo = models.TextField(max_length=100,default="tipo_prestamo", verbose_name="tipo de prestamo")
    
    fecha_solicitud = models.DateTimeField(auto_now_add=True, null=True, verbose_name="fecha de creación")
    fecha_modificacion = models.DateTimeField(auto_now_add=True, null=True, verbose_name="fecha de modificación")
    
    # user_id = models.models.ForeignKey(, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.id_solicitud