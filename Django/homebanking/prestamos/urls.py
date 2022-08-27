from django.urls import path, include
from .views import PrestamoDetail,SucursalList

urlpatterns = [
    path("prestamo/", PrestamoDetail.as_view()),
    path("sucursal/", SucursalList.as_view()),
]
