
from rest_framework import serializers
from tarjetas.models import Tarjeta


#item 5 
class TarjetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = "__all__"