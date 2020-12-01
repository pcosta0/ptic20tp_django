from django.db import models

class Paciente(models.Model):
    apellido = models.CharField('nombre del paciente', max_length = 50)
    nombre = models.CharField('apellido del paciente', max_length = 50)
    dni = models.CharField('dni del paciente', max_length = 10)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{str(self.apellido).capitalize()}, {str(self.nombre).capitalize()}'