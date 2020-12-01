from django import forms
from django.forms.widgets import NumberInput
from django.contrib.auth.models import User
from pacientes.models import Paciente
from .models import Producto
from django.forms import ModelChoiceField
import datetime

class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.first_name}, {obj.last_name}'

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'opcion', 'precio', 'activo']
    
    nombre = forms.CharField(widget = forms.TextInput(attrs={'autofocus': 'autofocus', 'class': 'form-control'})) 
    opcion = forms.CharField(required = False, widget = forms.TextInput(attrs={'class': 'form-control'}), help_text = 'Punto (.) separa grupos. Coma(,) separa opciones en grupos. Ej: rojo, verde, azul. arriba, abajo, derecha, izquierda') 
    precio = forms.CharField(initial = 0, required = False, widget = forms.NumberInput(attrs={'id': 'form_homework', 'step': '0.1', 'class': 'form-control'})) 
    activo = forms.BooleanField(required = False, initial = True) 
