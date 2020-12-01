from django import forms
from django.forms.widgets import NumberInput, DateTimeInput
from django.contrib.auth.models import User
from pacientes.models import Paciente
from .models import Turno
from django.forms import ModelChoiceField
import datetime

class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return F'{obj.last_name.title()}, {obj.first_name.title()}'

horarios =  [ (n*100 + m, str(n) + ':' + str(m).zfill(2)) for n in range(8, 19) for m in [0, 15, 30, 45]]
class FormCrearTurno(forms.ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'

    paciente = forms.ModelChoiceField(queryset=Paciente.objects.filter(activo=True), widget=forms.Select(attrs={'autofocus': 'autofocus', 'class': 'form-control'}))
    doctor = MyModelChoiceField(queryset=User.objects.filter(is_staff=False, groups__name='profesional'), widget=forms.Select(attrs={'class': 'form-control'}))
    fecha = forms.DateField(initial=datetime.date.today, widget=NumberInput(attrs={'type': 'date', 'class': 'form-control'}))
    hora = forms.ChoiceField(choices=horarios, widget=forms.Select(attrs={'class': 'form-control'}))    

opciones_fecha = [('0', 'Usar solo año'), ('1', 'Usar año y mes'), ('2', 'Usar año, mes y dia')]

class FormFiltroFecha(forms.Form):
    fecha = forms.DateField(initial=datetime.date.today, widget=NumberInput(attrs={'type': 'date', 'class': 'form-control'}) )
    opcionfecha = forms.CharField(label='Seleccione filtro', initial = opciones_fecha[1][0], widget = forms.RadioSelect(choices = opciones_fecha))
