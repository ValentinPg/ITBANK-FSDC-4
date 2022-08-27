from .models import Direccion, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets
from .serializers import UserClienteSerializer,DireccionSerializer
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
    
    


    
