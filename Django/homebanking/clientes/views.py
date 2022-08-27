from .models import Direccion, User
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics, viewsets
from .serializers import CuentaSerializer, PrestamoSerializer, UserClienteSerializer, TarjetasSerializer, SucursalSerializer, DireccionSerializer, SolicitudesPrestamosSerializer
from cuentas.models import Cuenta
from prestamos.models import Prestamo, Sucursal
from tarjetas.models import Tarjeta
from homebank.models import SolicitudesPrestamos
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
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
    permission_classes = [permissions.IsAdminUser]
    def get(self, request, pk):
        usuario = Tarjeta.objects.filter(customer_id = pk)
        serializer = TarjetasSerializer(usuario, many=True)
        if usuario:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
#item 6 y 7
class SolicitudesPrestamosViewset(viewsets.ModelViewSet):
    queryset = SolicitudesPrestamos.objects.all()
    serializer_class = SolicitudesPrestamosSerializer
    permission_classes = [permissions.IsAdminUser]
    
        
    
#item 8
class DireccionViewset(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def partial_update(self, request, pk, *arg, **kwargs):
        current_user = request.user
        if current_user.is_staff:
            print(pk)
            direccion = Direccion.objects.get(pk=pk)
            serializer = DireccionSerializer(direccion, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            current_pk = current_user.customer_id
            direccion = Direccion.objects.filter(customer_id=current_pk)
            serializer = DireccionSerializer(direccion, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
#item 9
class SucursalList(generics.ListAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    pagination_class = LimitOffsetPagination

    
