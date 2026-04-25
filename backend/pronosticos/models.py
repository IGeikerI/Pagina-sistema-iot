from django.db import models

class Pronostico(models.Model):
    ciudad = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    probabilidad_lluvia = models.FloatField()
    intensidad_lluvia = models.FloatField()
    descripcion = models.CharField(max_length=100)
    temperatura = models.FloatField()
    humedad = models.FloatField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ciudad} - {self.fecha}"