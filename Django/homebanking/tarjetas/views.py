from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import TarjetasSerializer
from tarjetas.models import Tarjeta


#item 5  
class TarjetasList(APIView):
    permission_classes = [permissions.IsAdminUser]
    def get(self, request, pk):
        usuario = Tarjeta.objects.filter(customer_id= pk)
        serializer = TarjetasSerializer(usuario, many=True)
        if usuario:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)