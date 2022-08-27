from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from clientes.models import Cliente
from homebank.models import SolicitudesPrestamos
from .forms import SolicitudPrestamo
from django.shortcuts import render
from rest_framework import permissions, viewsets
from .serializers import SolicitudesPrestamosSerializer
from homebank.models import SolicitudesPrestamos

@login_required
def vista(request):
    return render(request,"homebank/home.html")

@login_required
def formularioSolicitud(request):
    formulario_solicitud = SolicitudPrestamo
    current_user = request.user  #obtengo el usuario loggeado
    clienteId = current_user.customer_id
    
    if request.method == "POST":
        formulario_solicitud = formulario_solicitud(data=request.POST)
        
        if formulario_solicitud.is_valid():
            monto = request.POST.get("monto", "")
            fecha_inicio = request.POST.get("fecha_inicio", "")
            tipo_prestamo = request.POST.get("tipo_prestamo", "")
            customerMatch = Cliente.objects.filter(customer_id=clienteId)
            for x in customerMatch:
                tipo_cliente = x.tipoid
                if tipo_cliente == 1 and int(monto) > 100000: #Clientes Classic (se encuentra en la tabla tipos_cliente)
                    return redirect(reverse('prestamos')+ '?NO')
                elif tipo_cliente == 2 and monto > 300000: #Clientes Gold
                    return redirect(reverse('prestamos')+ '?NO')
                elif tipo_cliente == 3 and monto > 500000: #clientes Black
                    return redirect(reverse('prestamos')+ '?NO')
                else:
                    entry = SolicitudesPrestamos(monto=monto, fecha_inicio=fecha_inicio, tipo_prestamo=tipo_prestamo, customer_id=current_user.customer_id)
                    entry.save()
                    return redirect(reverse('prestamos')+ '?OK')
                
                    
    return render(request,"homebank/prestamos.html", {"form":formulario_solicitud})


#item 6 y 7
class SolicitudesPrestamosViewset(viewsets.ModelViewSet):
    queryset = SolicitudesPrestamos.objects.all()
    serializer_class = SolicitudesPrestamosSerializer
    permission_classes = [permissions.IsAdminUser]