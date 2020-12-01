from django.db import models
from pacientes.models import Paciente
from django.contrib.auth.models import User, Group

    
class HistorialObservacion(models.Model):    
    paciente = models.ForeignKey(Paciente, on_delete = models.RESTRICT, related_name='hcpacientes')
    doctor = models.ForeignKey(User, on_delete = models.RESTRICT, related_name='hcdoctores')
    fecha = models.DateField()
    observacion = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.fecha}: {self.observacion} '
