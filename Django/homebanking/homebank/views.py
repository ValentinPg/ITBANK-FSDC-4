from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import SolicitudPrestamo

@login_required
def vista(request):
    return render(request,"homebank/home.html")

@login_required
def formularioSolicitud(request):
    formulario_solicitud = SolicitudPrestamo
    
    if request.method == "POST":
        formulario_solicitud = formulario_solicitud(data=request.POST)
        
        if formulario_solicitud.is_valid():
            monto = request.POST.get("monto", "")
            fecha_inicio = request.POST.get("fecha_inicio", "")
            tipo_prestamo = request.POST.get("tipo_prestamo", "")
            
        return redirect(reverse('prestamos')+ '?OK')
    return render(request,"homebank/prestamos.html", {"form":formulario_solicitud})

