
from .models import User
from rest_framework import serializers
from cuentas.models import Cuenta
from prestamos.models import Prestamo, Sucursal
from tarjetas.models import Tarjeta

#item 1
class UserClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "email", "username", "customer_id" ]
        read_only_fields = ("id", "date_joined", "is_staff")
        

#item 2
class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ["cuentaid","balance"]
       
#item 3 
class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ["loan_type", "loan_total"]
       
#item 5 
class TarjetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = "__all__"
        
#item 9

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = "__all__"