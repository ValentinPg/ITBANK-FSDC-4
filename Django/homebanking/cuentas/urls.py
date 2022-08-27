from django.urls import path, include
from .views import  CuentaDetail

urlpatterns = [
    path("cuenta/", CuentaDetail.as_view()),
    ]