from django.urls import path, include
from .views import PrestamoDetail,SucursalList,PrestamoSucursalDetail

urlpatterns = [
    path("prestamo/", PrestamoDetail.as_view()),
    path("sucursal/", SucursalList.as_view()),
    path("prestamosu/<int:pk>", PrestamoSucursalDetail.as_view())
]
