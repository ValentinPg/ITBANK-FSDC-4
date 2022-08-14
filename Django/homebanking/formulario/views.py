from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def vista(request):
    return render(request,"formulario_prestamo/.html")

# Create your views here.
