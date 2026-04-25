from django.shortcuts import render
from rest_framework import viewsets
from .models import Prediccion
from .serializers import PrediccionSerializer

class PrediccionViewSet(viewsets.ModelViewSet):
    queryset = Prediccion.objects.all()
    serializer_class = PrediccionSerializer
