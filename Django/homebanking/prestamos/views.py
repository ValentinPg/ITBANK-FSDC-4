from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from .serializers import PrestamoSerializer, SucursalSerializer
from prestamos.models import Prestamo, Sucursal
from rest_framework.pagination import LimitOffsetPagination



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
    
    
#item 9
class SucursalList(generics.ListAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    pagination_class = LimitOffsetPagination