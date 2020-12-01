from django import forms
from django.forms.widgets import NumberInput
from django.contrib.auth.models import User
from pacientes.models import Paciente
from .models import Pedido, Producto, PedidoItem
from django.forms import ModelChoiceField
import datetime

class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.first_name}, {obj.last_name}'

class FormPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['fechahora', 'paciente', 'vendedor', 'tipopago', 'estado']

    fechahora = forms.DateField(initial=datetime.date.today, widget=NumberInput(attrs={'class': 'form-control', 'type': 'date'}))
    paciente = forms.ModelChoiceField(queryset=Paciente.objects.all(), widget=forms.Select(attrs={'autofocus': 'autofocus', 'class': 'form-control'}))
    vendedor = forms.ModelChoiceField(queryset=User.objects.all(), label='', widget=forms.Select(attrs={'hidden': 'True', 'class': 'form-control'}))
    tipopago = forms.ChoiceField(choices=Pedido.OPCIONES_DE_PAGO, widget=forms.Select(attrs={'class': 'form-control'}))
    estado = forms.ChoiceField(choices=Pedido.ESTADO_DE_PEDIDO, required=False, initial = Pedido.ESTADO_DE_PEDIDO[0][0], widget=forms.Select(attrs={'class': 'form-control'}))

class FormItemPedido(forms.ModelForm):
    class Meta:
        model = PedidoItem
        fields = ['cantidad', 'precio']

    cantidad = forms.IntegerField(initial=1, widget=NumberInput(attrs={'autofocus': 'autofocus', 'class': 'form-control'}))
    precio = forms.CharField(initial = 0, required = False, widget = forms.NumberInput(attrs={'id': 'form_homework', 'step': '0.1', 'class': 'form-control'})) 
