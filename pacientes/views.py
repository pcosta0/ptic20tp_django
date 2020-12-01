from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from usuarios.utilidades import *
from .models import Paciente
from turnos.models import Turno
from .forms import formCrearPaciente

def listado(request):
    contexto = logueadoComo(request, ['gerencia', 'secretaria'])
    if contexto: 
        contexto['pacientes'] = Paciente.objects.all()
        return render(request, "pacientes/listado.html", contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))
    
def CrearPaciente(request):
    contexto = logueadoComo(request, ['gerencia', 'secretaria'])
    if contexto: 
        if request.method == 'POST':
            form = formCrearPaciente(request.POST or None)
            if form.is_valid():
                form.save()    
                return HttpResponseRedirect(reverse("pacientes:listado"))
        else:
            form = formCrearPaciente()
            contexto['form'] = form 
            contexto['accion'] = 'Crear' 
            return render(request, 'pacientes/detalle.html', contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def ModificarPaciente(request, id_paciente):
    contexto = logueadoComo(request, ['gerencia', 'secretaria'])
    if contexto:     
        try:
            paciente = get_object_or_404(Paciente, id = id_paciente)
        except Exception:
            raise Http404('no existe el paciente')

        if request.method == 'POST':
            form = formCrearPaciente(request.POST, instance=paciente)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('pacientes:listado'))
        else:
            form = formCrearPaciente(instance=paciente)
            contexto['form'] = form 
            contexto['accion'] = 'Modificar' 
            return render(request, 'pacientes/detalle.html', contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def EliminarPaciente(request, id_paciente):
    contexto = logueadoComo(request, ['gerencia', 'secretaria'])
    if contexto:     
        try:
            paciente = get_object_or_404(Paciente, id = id_paciente)
            contexto['paciente'] = paciente
        except Exception:
            raise Http404('no existe el paciente')

        if request.method == 'POST':
            contexto['mensaje'] = request.POST['accion']
            if request.POST['accion'] == 'Eliminar':
                pass
                # paciente.delete() # aca eliminamos definitivmente al paciente 
            elif request.POST['accion'] == 'Desactivar':
                paciente.activo = not paciente.activo
                paciente.save()
            return HttpResponseRedirect(reverse('pacientes:listado'))
        else:
            contexto['accion'] = 'Eliminar' if (0 == (Turno.objects.filter(paciente__id = id_paciente).count())) else 'Desactivar'
            return render(request, 'pacientes/eliminar.html', contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))
