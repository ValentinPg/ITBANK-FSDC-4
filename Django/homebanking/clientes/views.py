from .models import User
from django.shortcuts import render
from .serializers import UserClienteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserDetail(APIView):
    def get(self, request):
        current_user = request.user
        current_pk = current_user.id
        usuario = User.objects.filter(id=current_pk).first()
        serializer = UserClienteSerializer(usuario)
        if usuario:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
