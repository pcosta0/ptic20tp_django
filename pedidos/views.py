from django.shortcuts import render, get_object_or_404, redirect
from usuarios.utilidades import *
from .models import Pedido, PedidoItem
from pacientes.models import Paciente
from .forms import *

def Listado(request):
    contexto = logueadoComo(request, ['gerencia', 'ventas'])
    if contexto: # es de ventas ?
        pedidos = Pedido.objects.filter() # obtiene la lista de pedidos
        contexto['pedidos'] = pedidos # guarda los pedidos en el contexto
        contexto['id_pedidoactual'] = request.session['id_pedidoactual'] if 'id_pedidoactual' in request.session else None # verifica id_pedidoactual en sesion
        return render(request, "pedidos/listado.html", contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def VerPedido(request, id_pedido):
    contexto = logueadoComo(request, ['gerencia', 'ventas'])
    if contexto: # es de ventas ?
        try:
            infopedido = get_object_or_404(Pedido, id = id_pedido)
            pedidos_det = PedidoItem.objects.filter(pedido_id=infopedido.id)
            # todo: crear total !!!
        except Exception:
            raise Http404('no existe el pedido')
        contexto['pedidos_det'] = pedidos_det
        contexto['id_pedidoactual'] = request.session['id_pedidoactual'] = infopedido.id # guarda el id info pedido en la sesion y contexto
        contexto['infopedidoactual'] = infopedido # guarda el info pedido en el contexto
        return render(request, 'pedidos/pedido.html', contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def CrearPedido(request):
    contexto = logueadoComo(request, ['gerencia', 'ventas'])
    if contexto: # es de ventas?
        vendedor = User.objects.get(id = contexto['id_usuario']) # busca al vendedor para el contexto                    contexto['id_pedidoactual'] = ''
        contexto['accion'] = 'Crear'
        form = FormPedido(request.POST or None)
        form.fields['vendedor'].initial = vendedor # se asigna el vendedor al form
        contexto['form'] = form # se guarda el form en el contexto
        if request.method == 'POST': # es un submit de crear pedido?
            if form.is_valid(): # es valido el form?
                infopedido = form.save() # se guarda el pedido y se asigna a infopedido
                contexto['id_pedidoactual'] = request.session['id_pedidoactual'] = infopedido.id # guarda el id info pedido en la sesion y contexto
                contexto['infopedidoactual'] = infopedido # guarda el info pedido en el contexto y la sesion
                return redirect("pedidos:verpedido", id_pedido = infopedido.id)
            else: # no es un from válido
                contexto['resultado'] = 'form no valido'
                return HttpResponseRedirect(reverse("paginas:inicio"))
        else: # es un nuevo pedido
            contexto['infopedidoactual'] = request.session['infopedidoactual'] = None
            return render(request, 'pedidos/infopedido.html', contexto)
    else: # no es de ventas
        return HttpResponseRedirect(reverse("paginas:inicio"))

def ModificarPedido(request, id_pedido):
    contexto = logueadoComo(request, ['gerencia', 'ventas'])
    if contexto: # es vendedor ?
        if id_pedido == 0: # si es 0 limpia la sesion del pedido actual
            contexto['id_pedidoactual'] = request.session['id_pedidoactual'] = ''
            return HttpResponseRedirect(reverse("pedidos:listado"))
        else:
            try:
                infopedido = get_object_or_404(Pedido, id = id_pedido)
            except Exception:
                raise Http404('no existe el pedido')

            contexto['id_pedidoactual'] = request.session['id_pedidoactual'] = infopedido.id
            contexto['infopedidoactual'] = infopedido # guarda el pedido en el contexto
            if request.method == 'POST':
                form = FormPedido(request.POST, instance = infopedido)
                if form.is_valid():
                    form.save()    
                    return redirect("pedidos:verpedido", id_pedido = infopedido.id)
                else:
                    contexto['form'] = form
                    return render(request, 'pedidos/infopedido.html', contexto)
            else:
                form = FormPedido(instance = infopedido)
                form.fields['fechahora'].initial = datetime.datetime.now() # infopedido.fechahora
                contexto['form'] = form
                return render(request, 'pedidos/infopedido.html', contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def EliminarPedido(request, id_pedido):
    pass

def SeleccionarItem(request):
    contexto = logueadoComo(request, ['gerencia', 'ventas'])
    if contexto: 
        try:
            id_pedido = request.session['id_pedidoactual'] # se obtiene el id_pedido actual de la sesion
            infopedido = get_object_or_404(Pedido, id = id_pedido) # se busca ese pedido en la bd
        except Exception:
            raise Http404('no hay pedido actual')

        contexto['id_pedidoactual'] = request.session['id_pedidoactual'] = infopedido.id
        contexto['infopedido'] = infopedido # guarda el pedido en el contexto

        items = Producto.objects.filter(activo=True)
        contexto['items'] = items
        return render(request, 'pedidos/seleccionaritem.html', contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def AgregarItem(request, id_pedido, id_item):
    contexto = logueadoComo(request, ['gerencia', 'ventas'])
    if contexto: 
        contexto['accion'] = 'Agregar item a pedido'
        try:
            infoPedido = get_object_or_404(Pedido, id = id_pedido)
            producto = get_object_or_404(Producto, id = id_item)
        except Exception:
            raise Http404('no existe el pedido o producto')

        opcion = producto.opcion # opcion = '1, 2, 3. a, b, c'
        op0 = [ [y.strip() for y in x.split(',')] for x in opcion.split('.')]
        contexto['opcion'] = op0 # op0 = '[[1, 2, 3],  [a, b, c]]'
        contexto['id_pedidoactual'] = request.session['id_pedidoactual'] = infoPedido.id # guarda el idpedidoactual en contexto y sesion
        contexto['infopedido'] = infoPedido # guarda el pedido en el contexto
        contexto['producto'] = producto #guarda el producto en el contexto

        if request.method == 'POST':
            sel_opc = [] # recupera las opciones seleccionadas
            for opc in op0: # recorre las opciones del item db
                if str(opc) in request.POST: # la opcion está en el post del form ?
                    sel_opc.append(request.POST[str(opc)]) # entonces agrega a la sel_opc 
            sel_opc = ', '.join(sel_opc)
            pedidoItemNuevo = PedidoItem(pedido=infoPedido, item=producto, cantidad=request.POST['cantidad'], precio=request.POST['precio'], opcion=sel_opc)            
            pedidoItemNuevo.save()
            return redirect("pedidos:verpedido", id_pedido = infoPedido.id)
        else:
            pedidoItemNuevo = PedidoItem(pedido=infoPedido, item=producto, cantidad=1, precio=producto.precio, opcion=producto.opcion)
            form = FormItemPedido(instance = pedidoItemNuevo)
            contexto['form'] = form
            return render(request, 'pedidos/editaritem.html', contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def ModificarItem(request, id_pedido, id_itempedido):
    contexto = logueadoComo(request, ['gerencia', 'ventas'])
    if contexto: 
        try:
            infoPedido = get_object_or_404(Pedido, id = id_pedido)
            pedidoItem = PedidoItem.objects.get(id = id_itempedido)
            producto = get_object_or_404(Producto, id = pedidoItem.item.id)
        except Exception:
            raise Http404('no se pudo recuperar la informacion del item')

        opcion = producto.opcion # opcion = '1, 2, 3. a, b, c'
        op0 = [ [y.strip() for y in x.split(',')] for x in opcion.split('.')]

        contexto['opcion'] = op0 # op0 = '[[1, 2, 3],  [a, b, c]]'
        contexto['id_pedidoactual'] = request.session['id_pedidoactual'] = infoPedido.id # guarda el idpedidoactual en contexto y sesion
        contexto['infopedido'] = infoPedido # guarda el pedido en el contexto
        contexto['producto'] = producto #guarda el producto en el contexto
        contexto['opcioneselegidas'] = [ op.strip() for op in pedidoItem.opcion.split(',')] # aca van las opciones elegidas del item de pedido

        if request.method == 'POST':
            form = FormItemPedido(request.POST, instance = pedidoItem)
            if form.is_valid():
                sel_opc = []
                for opc in op0: # recorre las opciones del item db
                    if str(opc) in request.POST: # la opcion está en el post del form ?
                        sel_opc.append(request.POST[str(opc)]) # entonces agrega a la sel_opc 
                sel_opc = ', '.join(sel_opc)
                pedidoItem.opcion = sel_opc
                pedidoItem.precio = precio=request.POST['precio']
                pedidoItem.cantidad = cantidad=request.POST['cantidad']
                pedidoItem.save()
                return redirect("pedidos:verpedido", id_pedido = infoPedido.id)
            else:
                print('>>>>>>>>>>> FORM NO VALIDO ')
        else:
            form = FormItemPedido(instance = pedidoItem)
            contexto['form'] = form
            return render(request, 'pedidos/editaritem.html', contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))
