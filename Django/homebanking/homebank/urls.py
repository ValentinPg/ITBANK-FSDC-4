
from django.urls import path
from . import views

urlpatterns = [
    path("homebank/", views.vista, name="homebank")
]
