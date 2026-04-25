from django.shortcuts import render

from rest_framework import viewsets
from .models import Alerta
from .serializers import AlertaSerializer

class AlertaViewSet(viewsets.ModelViewSet):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer
