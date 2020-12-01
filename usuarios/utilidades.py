from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, Group

def estado_auth(request):
    # todo: optimizar esto
    contexto = {}
    contexto['autenticado'] = request.user.is_authenticated
    contexto['usuario'] = request.user
    contexto['id_usuario'] = request.user.id
    contexto['grupos'] = [grupo['name'] for grupo in request.user.groups.all().values('name')]
    contexto['grupos_v'] = ', '.join(contexto['grupos'])
    contexto['id_pedidoactual'] = request.session['id_pedidoactual'] if 'id_pedidoactual' in request.session else None # verifica id_pedidoactual en sesion
    return contexto

def logueadoComo(request, grupo):
    # todo: optimizar esto
    pars = estado_auth(request)
    if set(grupo).intersection(pars['grupos']):
        return pars
