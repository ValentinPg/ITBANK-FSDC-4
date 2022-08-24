from .models import User
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import CuentaSerializer, PrestamoSerializer, UserClienteSerializer, TarjetasSerializer
from cuentas.models import Cuenta
from prestamos.models import Prestamo
from tarjetas.models import Tarjeta
#item 1
class UserDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        current_user = request.user
        current_pk = current_user.id
        usuario = User.objects.filter(id=current_pk).first()
        serializer = UserClienteSerializer(usuario)
        if usuario:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#item 2
class CuentaDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        current_user = request.user
        current_pk = current_user.customer_id
        usuario = Cuenta.objects.filter(customer_id=current_pk).first()
        serializer = CuentaSerializer(usuario)
        if usuario:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
   
#item 3 
class PrestamoDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        current_user = request.user
        current_pk = current_user.customer_id
        usuario = Prestamo.objects.filter(customer_id=current_pk)
        serializer = PrestamoSerializer(usuario, many=True)
        if usuario:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
  
#item 5  
class TarjetasList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        current_user = request.user
        usuario = Tarjeta.objects.filter(customer_id = pk)
        serializer = TarjetasSerializer(usuario, many=True)
        if current_user.is_staff:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    
