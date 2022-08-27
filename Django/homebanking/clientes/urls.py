
from django.urls import path, include
from .views import UserDetail,DireccionViewset
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'direccion', DireccionViewset)


urlpatterns = [
    path("user/", UserDetail.as_view()),
    path("",include(router.urls))
]
