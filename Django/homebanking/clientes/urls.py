from django.urls import path
from .views import UserDetail

urlpatterns = [
    path("clientes/<int:pk>/", UserDetail.as_view()),
]
