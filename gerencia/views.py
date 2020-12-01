from django.db.models import Count, Sum
from django.shortcuts import render
from usuarios.utilidades import *
from turnos.models import Turno
from pedidos.models import Pedido, PedidoItem
import datetime

def Informes(request):
    contexto = logueadoComo(request, ['gerencia'])
    if contexto: 

        return render(request, "gerencia/informes.html", contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))

def Informe(request, num_informe):
    contexto = logueadoComo(request, ['gerencia'])
    if contexto: 
        if num_informe == 1: 
            contexto['titulo'] = 'Pacientes atendidos en la ultima semana'
            contexto['informe'] = Turno.objects.filter(atendido=True, fecha__range=( datetime.datetime.now()-datetime.timedelta(days=7), datetime.datetime.now()) )
            return render(request, "gerencia/informe001.html", contexto)
        elif num_informe == 2: 
            contexto['titulo'] = 'Pacientes atendidos el ultimo mes'
            contexto['informe'] = Turno.objects.filter(atendido=True, fecha__range=( datetime.datetime.now()-datetime.timedelta(days=31), datetime.datetime.now()) )
            return render(request, "gerencia/informe001.html", contexto)
        elif num_informe == 3: 
            contexto['titulo'] = 'Pacientes no atendidos en la ultima semana'
            contexto['informe'] = Turno.objects.filter(atendido=False, fecha__range=( datetime.datetime.now()-datetime.timedelta(days=7), datetime.datetime.now()) )
            return render(request, "gerencia/informe001.html", contexto)
        elif num_informe == 4: 
            contexto['titulo'] = 'Pacientes no atendidos el ultimo mes'
            contexto['informe'] = Turno.objects.filter(atendido=False, fecha__range=( datetime.datetime.now()-datetime.timedelta(days=31), datetime.datetime.now()) )
            return render(request, "gerencia/informe001.html", contexto)
        elif num_informe == 5: 
            contexto['titulo'] = 'Pacientes que hicieron por lo menos un pedido en la semana'
            contexto['informe'] = Pedido.objects.filter(fechahora__range=( datetime.datetime.now()-datetime.timedelta(days=7), datetime.datetime.now()))
            return render(request, "gerencia/informe002.html", contexto)
        elif num_informe == 6: 
            contexto['titulo'] = 'Pacientes que hicieron por lo menos un pedido en el mes'
            contexto['informe'] = Pedido.objects.filter(fechahora__range=(datetime.datetime.now()-datetime.timedelta(days=31), datetime.datetime.now()))
            return render(request, "gerencia/informe002.html", contexto)
        elif num_informe == 7: 
            limite = 3
            contexto['titulo'] = f'Los {limite} productos mas vendidos en el mes'
            informe = PedidoItem.objects.only('item_id', 'item__nombre', 'cantidad').values('item__nombre').annotate(cantidad_total=Sum('cantidad')).order_by('-cantidad_total')[:limite]
            contexto['informe'] = informe
            return render(request, "gerencia/informe003.html", contexto)
        elif num_informe == 8: 
            contexto['titulo'] = f'Ventas totales del mes (ordenado por vendedor)'
            informe = Pedido.objects.only('vendedor', 'vendedor_str', 'vendedor__first_name', 'fechahora').values('vendedor__first_name', 'vendedor__last_name').annotate(cantidad_total=Count('vendedor')).order_by('-cantidad_total')
            print('>> Informe:', informe)
            for registro in informe:
                print(registro.values())
            contexto['informe'] = informe
            return render(request, "gerencia/informe004.html", contexto)
        else:
            return render(request, "gerencia/informes.html", contexto)
    else:
        return HttpResponseRedirect(reverse("paginas:inicio"))
