from django.db import models

# Create your models here.

class MarcasTarjeta(models.Model):
    marcaid = models.AutoField(db_column='marcaID', primary_key=True)  # Field name made lowercase.
    tipo_tarjeta = models.TextField()

    class Meta:
        managed = False
        db_table = 'marcas_tarjeta'
        
class Tarjeta(models.Model):
    tarjeta_id = models.AutoField(primary_key=True)
    numero = models.TextField(unique=True)
    cvv = models.IntegerField(db_column='CVV')  # Field name made lowercase.
    fecha_otorgamiento = models.TextField()
    fecha_expiracion = models.TextField()
    marcaid = models.IntegerField(db_column='marcaID', blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarjeta'
