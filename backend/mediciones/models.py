from django.db import models

class Medicion(models.Model):
    nivel_agua = models.FloatField()
    estado = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nivel_agua} cm - {self.estado}"