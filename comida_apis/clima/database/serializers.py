from rest_framework import serializers
from .models import persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = persona
        fields = ['id', 'nombre', 'email']

        