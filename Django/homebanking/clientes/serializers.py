

from .models import User, Direccion
from rest_framework import serializers


#item 1
class UserClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "email", "username", "customer_id" ]
        read_only_fields = ("id", "date_joined", "is_staff")
        

# #item 2
# class CuentaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cuenta
#         fields = ["cuentaid","balance"]
       
# #item 3 
# class PrestamoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Prestamo
#         fields = ["loan_type", "loan_total"]
       
# #item 5 
# class TarjetasSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tarjeta
#         fields = "__all__"

# #item 6 y 7
# class SolicitudesPrestamosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SolicitudesPrestamos
#         fields = "__all__"

#item 8
class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = "__all__"
        
#item 9

# class SucursalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sucursal
#         fields = "__all__"
#         read_only_fields = ("branch_id", "branch_number", "branch_name", "branch_address_id")