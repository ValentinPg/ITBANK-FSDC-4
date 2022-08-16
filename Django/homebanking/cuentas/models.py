from django.db import models

# Create your models here.

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    cuentaid = models.ForeignKey('TiposCuenta', models.DO_NOTHING, db_column='cuentaID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuenta'
        
class TiposCuenta(models.Model):
    cuentaid = models.AutoField(db_column='cuentaID', primary_key=True)  # Field name made lowercase.
    cuenta_cliente = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipos_cuenta'
