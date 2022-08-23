
from .models import User
from rest_framework import serializers

class UserClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "email", "username", "customer_id" ]
        read_only_fields = ("id", "date_joined", "is_staff")