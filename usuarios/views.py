from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .utilidades import estado_auth

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("usuarios:login"))
    return render(request, "usuarios/bienvenida.html", estado_auth(request))

def vista_login(request):
    if request.user.is_authenticated:
        return render(request, "usuarios/bienvenida.html", estado_auth(request))
    else:
        if request.method == "POST":
            usuario = request.POST["usuario"]
            clave = request.POST["clave"]
            user = authenticate(request, username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("usuarios:index"))
            else:
                return render(request, "usuarios/login.html", {
                    "mensage": "Credenciales no validas"
                })
        else:
            return render(request, "usuarios/login.html")

def vista_logout(request):
    logout(request)
    return render(request, "usuarios/login.html", {
        "mensage": "Deslogueado"
    })