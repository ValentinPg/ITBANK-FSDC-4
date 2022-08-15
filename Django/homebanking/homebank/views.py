from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from clientes.models import User

from homebank.models import SolicitudesPrestamos

from .forms import SolicitudPrestamo

@login_required
def vista(request):
    return render(request,"homebank/home.html")

@login_required
def formularioSolicitud(request):
    formulario_solicitud = SolicitudPrestamo
    current_user = request.user  #obtengo el usuario loggeado
    
    if request.method == "POST":
        formulario_solicitud = formulario_solicitud(data=request.POST)
        
        if formulario_solicitud.is_valid():
            monto = request.POST.get("monto", "")
            fecha_inicio = request.POST.get("fecha_inicio", "")
            tipo_prestamo = request.POST.get("tipo_prestamo", "")
            
            entry = SolicitudesPrestamos(monto=monto, fecha_inicio=fecha_inicio, tipo_prestamo=tipo_prestamo, usuario=current_user.customer_id)
            entry.save()
                      
        return redirect(reverse('prestamos')+ '?OK')
    return render(request,"homebank/prestamos.html", {"form":formulario_solicitud})

