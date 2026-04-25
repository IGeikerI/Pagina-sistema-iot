from rest_framework import serializers
from .models import Pronostico

class PronosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pronostico
        fields = '__all__'