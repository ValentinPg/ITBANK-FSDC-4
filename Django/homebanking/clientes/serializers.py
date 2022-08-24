
from .models import User
from rest_framework import serializers
from cuentas.models import Cuenta
from prestamos.models import Prestamo

class UserClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "email", "username", "customer_id" ]
        read_only_fields = ("id", "date_joined", "is_staff")
        


class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ["cuentaid","balance"]
        
class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ["loan_type", "loan_total"]