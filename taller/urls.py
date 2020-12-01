from django.urls import path
from . import views

app_name = 'taller'

urlpatterns = [
    path("", views.Listado, name="listado"),
    path("<int:id_pedido>/verpedido", views.VerPedido, name="verpedido"),
    path("<int:id_pedido>/cambiarestado", views.CambiarEstado, name="cambiarestado"),
]