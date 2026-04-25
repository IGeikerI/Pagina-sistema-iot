from django.db import models
from mediciones.models import Medicion
from pronosticos.models import Pronostico

class HistorialPrediccion(models.Model):
    medicion = models.ForeignKey(Medicion, on_delete=models.CASCADE)
    pronostico = models.ForeignKey(Pronostico, on_delete=models.CASCADE)
    riesgo_calculado = models.CharField(max_length=20)
    observacion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.riesgo_calculado
