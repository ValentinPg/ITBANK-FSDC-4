from django.urls import path, include
from .views import  SolicitudesPrestamosViewset
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'solicitud', SolicitudesPrestamosViewset)

urlpatterns = [
    path("homebank/", views.vista, name="homebank"),
    path("prestamos/", views.formularioSolicitud, name="formularios"),
    path("",include(router.urls))
]
