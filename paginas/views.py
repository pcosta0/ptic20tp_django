from django.shortcuts import render
from usuarios.utilidades import estado_auth

def vista_inicio(request):
    return render(request, 'paginas/inicio.html', estado_auth(request))

def vista_acercade(request):
    return render(request, 'paginas/acercade.html', estado_auth(request))

