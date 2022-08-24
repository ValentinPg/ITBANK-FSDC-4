from django.urls import path
from .views import UserDetail, CuentaDetail

urlpatterns = [
    path("user/", UserDetail.as_view()),
    path("cuenta/", CuentaDetail.as_view()),
]
