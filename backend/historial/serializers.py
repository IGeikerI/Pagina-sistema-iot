from rest_framework import serializers
from .models import HistorialPrediccion

class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialPrediccion
        fields = '__all__'