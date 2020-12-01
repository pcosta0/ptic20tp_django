from django.db import models
from pacientes.models import Paciente
from django.contrib.auth.models import User, Group

class Turno(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete = models.RESTRICT, limit_choices_to={'activo': True}, related_name='turnopacientes')
    doctor = models.ForeignKey(User, on_delete = models.RESTRICT, related_name='turnodoctores')
    fecha = models.DateField()
    hora = models.IntegerField()
    atendido = models.BooleanField(default=False)

    class Meta:
        ordering = ['fecha', 'hora']
    
    def __str__(self):
        return f'{self.paciente.apellido.capitalize}, {self.paciente.nombre.capitalize}'

    def hora_str(self):
        strhora = str(self.hora)
        return strhora[:-2]+':'+strhora[-2:]

    def doctor_str(self):
        return self.doctor.first_name.capitalize() + ', ' + self.doctor.last_name.capitalize()