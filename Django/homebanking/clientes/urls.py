from django.urls import path
from .views import PrestamoDetail, UserDetail, CuentaDetail, TarjetasList

urlpatterns = [
    path("user/", UserDetail.as_view()),
    path("cuenta/", CuentaDetail.as_view()),
    path("prestamo/", PrestamoDetail.as_view()),
    path("tarjeta/<int:pk>", TarjetasList.as_view()),
]
