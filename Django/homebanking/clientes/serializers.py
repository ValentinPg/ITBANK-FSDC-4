

from .models import User, Direccion
from rest_framework import serializers


#item 1
class UserClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "email", "username", "customer_id" ]
        read_only_fields = ("id", "date_joined", "is_staff")
        



#item 8
class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = "__all__"
        
