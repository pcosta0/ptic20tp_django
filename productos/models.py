from django.db import models
 
class Producto(models.Model):    
    nombre = models.CharField(max_length=200) 
    opcion = models.CharField(max_length=500)
    precio = models.FloatField()
    activo = models.BooleanField()

    def __str__(self):
        return f'{self.nombre}'
