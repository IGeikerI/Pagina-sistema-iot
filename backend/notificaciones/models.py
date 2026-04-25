from django.db import models
from usuarios.models import Usuario
from alertas.models import Alerta

class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    alerta = models.ForeignKey(Alerta, on_delete=models.CASCADE)
    leida = models.BooleanField(default=False)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notificación a {self.usuario.nombre}"
