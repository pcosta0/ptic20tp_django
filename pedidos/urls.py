from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path("", views.Listado, name="listado"),
    path("crear", views.CrearPedido, name="crearpedido"),
    path("<int:id_pedido>", views.VerPedido, name="verpedido"),
    path("<int:id_pedido>/modificar", views.ModificarPedido, name="modificarpedido"),
    path("<int:id_pedido>/eliminar", views.EliminarPedido, name="eliminarpedido"),
    path("seleccionaritem", views.SeleccionarItem, name="seleccionaritem"),
    path("<int:id_pedido>/agregaritem/<int:id_item>", views.AgregarItem, name="agregaritem"),
    path("<int:id_pedido>/modificaritem/<int:id_itempedido>", views.ModificarItem, name="modificaritem"),
]