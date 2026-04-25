from django.db import models
from predicciones.models import Prediccion

class Alerta(models.Model):
    prediccion = models.ForeignKey(Prediccion, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    nivel_riesgo = models.CharField(max_length=20)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tipo