
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics, viewsets
from .serializers import CuentaSerializer
from cuentas.models import Cuenta


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
    

