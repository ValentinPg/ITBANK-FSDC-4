from rest_framework import serializers
from homebank.models import SolicitudesPrestamos

#item 6 y 7
class SolicitudesPrestamosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudesPrestamos
        fields = "__all__"