from rest_framework import viewsets
from .models import persona
from .serializers import PersonaSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = persona.objects.all()
    serializer_class = PersonaSerializer


