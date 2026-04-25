from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    rol = models.CharField(max_length=20)
    barrio = models.CharField(max_length=100)
    estado = models.CharField(max_length=20)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre