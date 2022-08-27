from rest_framework import serializers
from prestamos.models import Prestamo, Sucursal



#item 3 
class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ["loan_type", "loan_total"]
        
#item 4
class PrestamoSucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ["loan_type","loan_total","sucursal_name"]
 
#item 9        
class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = "__all__"
        read_only_fields = ("branch_id", "branch_number", "branch_name", "branch_address_id")