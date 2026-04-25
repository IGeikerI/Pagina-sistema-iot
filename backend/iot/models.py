from django.db import models


# 🔹 ZONA
class ZonaMonitoreo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    ubicacion = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre


# 🔹 DISPOSITIVO (ESP32)
class DispositivoIoT(models.Model):
    nombre = models.CharField(max_length=100)
    zona = models.ForeignKey(ZonaMonitoreo, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, default="activo")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


# 🔹 SENSOR
class Sensor(models.Model):
    tipo = models.CharField(max_length=50)  # ultrasonido, temperatura, etc
    dispositivo = models.ForeignKey(DispositivoIoT, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo


# 🔹 LECTURA DE NIVEL
class LecturaNivel(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    nivel_agua = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nivel_agua} cm"


# 🔹 ESTADO DE RIESGO
class EstadoRiesgo(models.Model):
    nombre = models.CharField(max_length=20)  # NORMAL, ALERTA, PELIGRO

    def __str__(self):
        return self.nombre


# 🔹 PREDICCIÓN DE RIESGO
class PrediccionRiesgo(models.Model):
    fecha = models.DateField()
    probabilidad_lluvia = models.FloatField()
    riesgo = models.ForeignKey(EstadoRiesgo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fecha} - {self.riesgo}"


# 🔹 ACTUADOR
class Actuador(models.Model):
    nombre = models.CharField(max_length=100)
    dispositivo = models.ForeignKey(DispositivoIoT, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


# 🔹 ESTADO DEL ACTUADOR
class EstadoActuador(models.Model):
    actuador = models.ForeignKey(Actuador, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20)  # ON / OFF
    fecha = models.DateTimeField(auto_now_add=True)


# 🔹 COMANDO REMOTO
class ComandoRemoto(models.Model):
    actuador = models.ForeignKey(Actuador, on_delete=models.CASCADE)
    comando = models.CharField(max_length=50)  # encender, apagar
    fecha = models.DateTimeField(auto_now_add=True)


# 🔹 RESPUESTA DEL DISPOSITIVO
class RespuestaComando(models.Model):
    comando = models.ForeignKey(ComandoRemoto, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)


# 🔹 ROL
class Rol(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


# 🔹 USUARIO - ROL
class UsuarioRol(models.Model):
    usuario_id = models.IntegerField()
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)


# 🔹 AUDITORÍA
class AuditoriaSistema(models.Model):
    accion = models.CharField(max_length=200)
    usuario_id = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)