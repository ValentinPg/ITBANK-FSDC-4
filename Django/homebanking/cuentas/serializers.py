from rest_framework import serializers
from .models import Cuenta

#item 2
class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ["cuentaid","balance"]