from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django import forms
from datetime import datetime
from usuarios.utilidades import *
from .models import Turno
from .forms import FormCrearTurno, FormFiltroFecha

def Listado(request):
    contexto = logueadoComo(request, ['gerencia', 'profesional', 'secretaria'])
    if contexto: 
        if 'profesional' in contexto['grupos']: # es un doctor?
            turnos = Turno.objects.filter(doctor = request.user) # filtra solo sus pacientes
        else:
            turnos = Turno.objects.all().order_by('-fecha', '-hora')

        if request.method == 'POST': # form posteado con valores ?
            form = FormFiltroFecha(initial = request.POST) # carga el form con valores posteados

            anio = request.POST['fecha'][0:4]
            mes = request.POST['fecha'][5:7]
            dia = request.POST['fecha'][8:10]
            opcionfecha = request.POST['opcionfecha']

            if opcionfecha == '0':
                turnos = turnos.filter(fecha__year=anio)
                contexto['filtro'] = f'Año = {anio}'
            elif opcionfecha == '1':
                turnos = turnos.filter(fecha__year=anio, fecha__month=mes)
                contexto['filtro'] = f'Mes / Año = {mes} / {anio}'
            elif opcionfecha == '2':
                turnos = turnos.filter(fecha__year=anio, fecha__month=mes, fecha__day=dia)
                contexto['filtro'] = f'Fecha = {dia} / {mes} / {anio}'
        else: # inicial sin post
            anio = datetime.now().year
            mes = datetime.now().month
            turnos = turnos.filter(fecha__year = anio, fecha__month = mes)
            contexto['filtro'] =  f'Mes / Año = {mes} / {anio}'
            form = FormFiltroFecha(initial = {'usarmes': True, 'usardia': False})

        contexto['form'] = form
        contexto['turnos'] = turnos
        print('Filtro: ', contexto['filtro'])
        return render(request, "turnos/listado.html", contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))
    
def CrearTurno(request):
    contexto = logueadoComo(request, ['gerencia', 'secretaria'])
    if contexto: 
        contexto['accion'] = 'Crear'
        form = FormCrearTurno(request.POST or None)
        contexto['form'] = form
        if request.method == 'POST':
            if form.is_valid():
                form.save()    
                contexto['resultado'] = 'form valido'
                return HttpResponseRedirect(reverse("turnos:listado"))
            else:
                contexto['resultado'] = 'form no valido'
                return render(request, 'turnos/detalle.html', contexto)
        else:
            contexto['resultado'] = 'form nuevo'
            return render(request, 'turnos/detalle.html', contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def ModificarTurno(request, id_turno):
    contexto = logueadoComo(request, ['gerencia', 'secretaria'])
    if contexto: 
        contexto['accion'] = 'Modificar'
        try:
            turno = get_object_or_404(Turno, id = id_turno)
        except Exception:
            raise Http404('no existe el turno')

        if request.method == 'POST':
            form = FormCrearTurno(request.POST, instance = turno)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('turnos:listado'))
        else:
            form = FormCrearTurno(instance = turno)
            contexto['form'] = form
            return render(request, 'turnos/detalle.html', contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def EliminarTurno(request, id_turno):
    contexto = logueadoComo(request, ['gerencia', 'secretaria'])
    if contexto:     
        try:
            turno = get_object_or_404(Turno, id = id_turno)
            contexto['turno'] = turno
        except Exception:
            raise Http404('no existe el turno')

        if request.method == 'POST':
            turno.delete()
            return HttpResponseRedirect(reverse('turnos:listado'))
        else:
            return render(request, 'turnos/eliminar.html', contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def AlternarAtendido(request, id_turno):
    contexto = logueadoComo(request, ['gerencia', 'profesional', 'secretaria'])
    if contexto: 
        try:
            turno = get_object_or_404(Turno, id = id_turno)
        except Exception:
            raise Http404('no existe el turno')
        turno.atendido = not turno.atendido
        turno.save()
        return HttpResponseRedirect(reverse('turnos:listado'))
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))
