from django.shortcuts import render, get_object_or_404, redirect
from usuarios.utilidades import *
from .models import Producto
from .forms import FormProducto

def Listado(request):
    contexto = logueadoComo(request, ['gerencia', 'ventas'])
    if contexto: 
        productos = Producto.objects.filter()
        contexto['productos'] = productos
        contexto['id_pedidoactual'] = request.session['id_pedidoactual'] if 'id_pedidoactual' in request.session else None # verifica id_pedidoactual en sesion
        return render(request, "productos/listado.html", contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def CrearProducto(request):
    contexto = logueadoComo(request, ['gerencia', 'ventas'])
    if contexto: 
        contexto['accion'] = 'Crear'
        form = FormProducto(request.POST or None)
        contexto['form'] = form
        if request.method == 'POST':
            if form.is_valid():
                form.save()    
                contexto['resultado'] = 'form valido'
                return HttpResponseRedirect(reverse("productos:listado"))
            else:
                contexto['resultado'] = 'form no valido'
                return render(request, 'productos/detalle.html', contexto)
        else:
            contexto['resultado'] = 'form nuevo'
            return render(request, 'productos/detalle.html', contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def ModificarProducto(request, id_producto):
    contexto = logueadoComo(request, ['gerencia', 'ventas'])
    if contexto: 
        contexto['accion'] = 'Modificar'
        try:
            producto = get_object_or_404(Producto, id = id_producto)
        except Exception:
            raise Http404('no existe el producto')

        if request.method == 'POST':
            form = FormProducto(request.POST, instance = producto)
            if form.is_valid():
                form.save()    
                contexto['resultado'] = 'form valido'
                return HttpResponseRedirect(reverse("productos:listado"))
            else:
                contexto['form'] = form
                contexto['resultado'] = 'form no valido'
                return render(request, 'productos/detalle.html', contexto)
        else:
            form = FormProducto(instance = producto)
            contexto['form'] = form
            contexto['resultado'] = 'form nuevo'
            return render(request, 'productos/detalle.html', contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def EliminarProducto(request, id_producto):
    contexto = logueadoComo(request, ['gerencia', 'ventas'])
    if contexto: 
        contexto['accion'] = 'Eliminar'
        try:
            producto = get_object_or_404(Producto, id = id_producto)
            # todo: verificar que no hayan registros relacionados en pedidos y si es asi solo ofrecer desactivar
        except Exception:
            raise Http404('no existe el producto')

        contexto['producto'] = producto
        if request.method == 'POST':
            # todo: aca se elimina o desactiva el producto
            return HttpResponseRedirect(reverse("productos:listado"))
        else:
            return render(request, 'productos/eliminar.html', contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))
