from django import forms
from .models import Paciente

class formCrearPaciente(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

    apellido = forms.CharField(widget = forms.TextInput(attrs={'autofocus': 'autofocus', 'class': 'form-control'})) 
    nombre = forms.CharField(widget = forms.TextInput(attrs={ 'class': 'form-control'})) 
    dni = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'})) 
    activo = forms.BooleanField(initial=True, required = False) 
