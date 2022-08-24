from django.urls import path
from .views import PrestamoDetail, UserDetail, CuentaDetail

urlpatterns = [
    path("user/", UserDetail.as_view()),
    path("cuenta/", CuentaDetail.as_view()),
    path("prestamo/", PrestamoDetail.as_view()),
]
