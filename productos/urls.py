from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path("", views.Listado, name="listado"),
    path("crear", views.CrearProducto, name="crearproducto"),
    path("<int:id_producto>/modificar", views.ModificarProducto, name="modificarproducto"),
    path("<int:id_producto>/eliminar", views.EliminarProducto, name="eliminarproducto"),
]