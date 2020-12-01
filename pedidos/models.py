from django.db import models
from pacientes.models import Paciente
from productos.models import Producto
from django.contrib.auth.models import User, Group


class Pedido(models.Model):    
    ESTADO_DE_PEDIDO = [
        (0, 'pendiente'),
        (1, 'pedido'),
        (2, 'taller'),
        (3, 'finalizado'),
    ]
    OPCIONES_DE_PAGO = [
        (0, 'tarjeta de credito'),
        (1, 'tarjeta de debito'),
        (2, 'villetera virtual'),
        (3, 'efectivo'),
    ]
    fechahora = models.DateField() #models.DateTimeField()
    paciente = models.ForeignKey(Paciente, on_delete = models.RESTRICT, related_name='pedidopacientes')
    vendedor = models.ForeignKey(User, on_delete = models.RESTRICT, related_name='pedidovendedores')
    tipopago = models.IntegerField(choices=OPCIONES_DE_PAGO, default=1)
    estado = models.IntegerField(choices=ESTADO_DE_PEDIDO, default=1)
    
    def estado_str(self):
        return self.ESTADO_DE_PEDIDO[self.estado][1]

    def tipopago_str(self):
        return self.OPCIONES_DE_PAGO[self.tipopago][1]

    def vendedor_str(self):
        return self.vendedor.first_name.capitalize() + ', ' + self.vendedor.last_name.capitalize()

class PedidoItem(models.Model):    
    pedido = models.ForeignKey(Pedido, on_delete = models.CASCADE, related_name='pedidodeitem')
    item = models.ForeignKey(Producto, on_delete = models.RESTRICT, related_name='productodeitem') 
    cantidad = models.IntegerField(default=1)
    precio = models.FloatField(default=0)
    opcion = models.CharField(max_length=500)

    def __str__(self): 
        return self.item.nombre.capitalize() + ('' if self.opcion.strip() == '' else ' - ') + self.opcion.capitalize()

    def subtotal(self):
        return self.precio * self.cantidad