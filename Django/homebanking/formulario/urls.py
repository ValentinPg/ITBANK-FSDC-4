
from django.urls import path
from . import views

urlpatterns = [
    path("formulario_prestamo/", views.vista, name="formulario")
]
