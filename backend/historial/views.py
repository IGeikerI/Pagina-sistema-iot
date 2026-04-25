from django.shortcuts import render

from rest_framework import viewsets
from .models import HistorialPrediccion
from .serializers import HistorialSerializer

class HistorialViewSet(viewsets.ModelViewSet):
    queryset = HistorialPrediccion.objects.all()
    serializer_class = HistorialSerializer