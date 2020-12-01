from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from usuarios.utilidades import *
from pedidos.models import Pedido, PedidoItem

def Listado(request):
    contexto = logueadoComo(request, ['gerencia', 'taller'])
    if contexto: 
        pedidos = Pedido.objects.filter(Q(estado=2) | Q(estado=3)) # obtiene la lista de pedidos
        contexto['pedidos'] = pedidos # guarda los pedidos en el contexto
        contexto['id_pedidoactual'] = request.session['id_pedidoactual'] if 'id_pedidoactual' in request.session else None # verifica id_pedidoactual en sesion
        return render(request, "taller/listado.html", contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def VerPedido(request, id_pedido):
    contexto = logueadoComo(request, ['gerencia', 'taller'])
    if contexto: 
        try:
            infopedido = get_object_or_404(Pedido, id = id_pedido)
            pedidos_det = PedidoItem.objects.filter(pedido_id=infopedido.id)
        except Exception:
            raise Http404('no existe el pedido')
        contexto['pedidos_det'] = pedidos_det
        contexto['id_pedidoactual'] = request.session['id_pedidoactual'] = infopedido.id # guarda el id info pedido en la sesion y contexto
        contexto['infopedidoactual'] = infopedido # guarda el info pedido en el contexto
        return render(request, 'taller/pedido.html', contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def CambiarEstado(request, id_pedido):
    contexto = logueadoComo(request, ['gerencia', 'taller'])
    if contexto: 
        try:
            infopedido = get_object_or_404(Pedido, id = id_pedido)
        except Exception:
            raise Http404('no existe el pedido')
        if infopedido.estado == 2:
            infopedido.estado = 3
        else:
            infopedido.estado = 2
        infopedido.save()
        return HttpResponseRedirect(reverse("taller:listado"))
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))
