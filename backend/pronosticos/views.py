from django.shortcuts import render

from rest_framework import viewsets
from .models import Pronostico
from .serializers import PronosticoSerializer

class PronosticoViewSet(viewsets.ModelViewSet):
    queryset = Pronostico.objects.all()
    serializer_class = PronosticoSerializer
