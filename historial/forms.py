from django import forms
from django.forms.widgets import NumberInput
from django.contrib.auth.models import User
from pacientes.models import Paciente
from .models import HistorialObservacion
from django.forms import ModelChoiceField
import datetime

class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.first_name}, {obj.last_name}'

class FormCrearObservacion(forms.ModelForm):
    class Meta:
        model = HistorialObservacion
        fields = ['fecha',  'observacion']
    
    fecha = forms.DateField(initial = datetime.date.today, widget = NumberInput(attrs={'autofocus': 'autofocus', 'type': 'date', 'class': 'form-control'}))
    observacion = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-control'})) 

opciones_fecha = [('0', 'Usar solo año'), ('1', 'Usar año y mes'), ('2', 'Usar año, mes y dia')]

