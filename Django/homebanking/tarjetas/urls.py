from django.urls import path, include
from .views import TarjetasList


urlpatterns = [
    path("tarjeta/<int:pk>", TarjetasList.as_view()),
]