
from django.urls import path, include
from .views import PrestamoDetail, UserDetail, CuentaDetail, TarjetasList, SucursalList, DireccionViewset, SolicitudesPrestamosViewset
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'direccion', DireccionViewset)
router.register(r'solicitud', SolicitudesPrestamosViewset)


urlpatterns = [
    path("user/", UserDetail.as_view()),
    path("cuenta/", CuentaDetail.as_view()),
    path("prestamo/", PrestamoDetail.as_view()),
    path("tarjeta/<int:pk>", TarjetasList.as_view()),
    path("sucursal/", SucursalList.as_view()), 
    path("",include(router.urls))
]
