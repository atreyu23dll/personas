from django.urls import path, include
from rest_framework import routers
from .views import PersonaViewSet

router = routers.DefaultRouter()
router.register(r'personas', PersonaViewSet, basename='persona')

urlpatterns = [
    path('', include(router.urls)), 
]