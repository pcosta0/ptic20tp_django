from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django import forms
from datetime import datetime
from usuarios.utilidades import *
from .models import HistorialObservacion
from pacientes.models import Paciente
from turnos.models import Turno
from .forms import FormCrearObservacion

def Listado(request):
    contexto = logueadoComo(request, ['gerencia', 'profesional'])
    if contexto: 
        if 'gerencia' in contexto['grupos']:
            pacientes = Turno.objects.filter() # el gerente ve todos los historiales
        else:
            pacientes = Turno.objects.filter(doctor = request.user) # los doctores solo ven aquienes atendieron
        pacientesunicos = []
        for pc in pacientes:
            if pc.paciente not in pacientesunicos:
                pacientesunicos.append(pc.paciente)
        contexto['pacientes'] = pacientesunicos
        return render(request, "historial/listadopacientes.html", contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def HistorialPaciente(request, id_paciente):
    contexto = logueadoComo(request, ['gerencia', 'profesional'])
    if contexto: 
        try:
            print('doc id: ', contexto['id_usuario'])
            print('paciente id: ', id_paciente)

            paciente = get_object_or_404(Paciente, id = id_paciente) # verifica exstencia de paciente
            turnos = Turno.objects.filter(paciente_id = id_paciente, doctor_id = contexto['id_usuario']) # verifica que el doctor haya atendido al paciente 
        except Exception:
            raise Http404('no existe el paciente ')

        contexto['paciente'] = paciente
        observaciones = HistorialObservacion.objects.filter(paciente_id = id_paciente)
        contexto['observaciones'] = observaciones
        return render(request, "historial/historialpaciente.html", contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def CrearObservacion(request, id_paciente):
    contexto = logueadoComo(request, ['gerencia', 'profesional']) # solo profesional accede a esto
    if contexto: # hay contexto entonces es profesional 
        contexto['accion'] = 'Crear' 
        try: # se busca el paciente y luego turnos del paciente filtrados con el profesional actual
            paciente = get_object_or_404(Paciente, id = id_paciente)
            turnos = Turno.objects.filter(paciente_id = id_paciente, doctor_id = contexto['id_usuario'])
            if turnos.count() == 0: # no hay registros?
                raise Http404()  
        except Exception: # no hay pacientes atendidos por el doctor
            raise Http404('no existe el paciente o doctor')
        contexto['paciente'] = paciente

        form = FormCrearObservacion(request.POST or None)
        print('Formulario: ', form)
        if request.method == 'POST':
            if form.is_valid():
                doctor = User.objects.get(id = contexto['id_usuario'])
                fecha = request.POST['fecha']
                observacion = HistorialObservacion(paciente = paciente, doctor = doctor, fecha = fecha, observacion = request.POST['observacion'])
                observacion.save()
                return redirect("historial:historialpaciente", id_paciente = id_paciente)
        else:
            contexto['form'] = form 
            return render(request, "historial/detalleobservacion.html", contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def ModificarObservacion(request, id_observacion):
    contexto = logueadoComo(request, ['gerencia', 'profesional']) # solo profesional accede a esto
    if contexto: # hay contexto entonces es profesional 
        contexto['accion'] = 'Modificar' 
        try: # se busca la observacion y paciente
            observacion = get_object_or_404(HistorialObservacion, id = id_observacion)
            paciente = observacion.paciente
            if not observacion.doctor_id == contexto['id_usuario']:
                raise()
        except Exception:
            raise Http404('no existe la observacion')
        # se agregan los resultados al contexto
        contexto['observacion'] = observacion
        contexto['paciente'] = paciente

        if request.method == 'POST': # el usuario confirmó la modificacion mediante POST?
            form = FormCrearObservacion(request.POST, instance = observacion)
            if form.is_valid():
                observacion.save()
                return redirect("historial:historialpaciente", id_paciente = paciente.id) 
        else: # es la carga inicial de la pagina modificar
            form = FormCrearObservacion(instance = observacion)
            print('>>> form: ', form)
            contexto['form'] = form 
            return render(request, "historial/detalleobservacion.html", contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def EliminarObservacion(request, id_observacion):
    contexto = logueadoComo(request, ['gerencia', 'profesional']) # solo profesional accede a esto
    if contexto: # hay contexto entonces es profesional
        try: # se busca la observacion y paciente
            observacion = get_object_or_404(HistorialObservacion, id = id_observacion)
            paciente = observacion.paciente
        except Exception:
            raise Http404('no existe la observacion')
        # se agregan los resultados al contexto
        contexto['observacion'] = observacion
        contexto['paciente'] = paciente

        if request.method == 'POST': # el usuario confirmó la eliminacion mediante POST?
            observacion.delete()
            return redirect("historial:historialpaciente", id_paciente=paciente.id) 
        else: # es la carga inicial de la pagina eliminar
            return render(request, "historial/eliminarobservacion.html", contexto)
    else: #no es profesional
        return HttpResponseRedirect(reverse("paginas:inicio"))
