from django.contrib import admin
from .models import *

admin.site.register(ZonaMonitoreo)
admin.site.register(DispositivoIoT)
admin.site.register(Sensor)
admin.site.register(LecturaNivel)
admin.site.register(EstadoRiesgo)
admin.site.register(PrediccionRiesgo)
admin.site.register(Actuador)
admin.site.register(EstadoActuador)
admin.site.register(ComandoRemoto)
admin.site.register(RespuestaComando)
admin.site.register(Rol)
admin.site.register(UsuarioRol)
admin.site.register(AuditoriaSistema)
