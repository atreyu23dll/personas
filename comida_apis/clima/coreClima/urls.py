from django.urls import path
from .views import home, registrar_usuario

urlpatterns = [
    path("", home, name="home"),
    path("registrar/", registrar_usuario, name="registrar_usuario"),
]
