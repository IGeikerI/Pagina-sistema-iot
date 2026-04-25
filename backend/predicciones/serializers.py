from rest_framework import serializers
from .models import Prediccion

class PrediccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediccion
        fields = '__all__'