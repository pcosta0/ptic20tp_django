from django.urls import path
from . import views

app_name = 'turnos'

urlpatterns = [
    path("", views.Listado, name="listado"),
    path("crear/", views.CrearTurno, name="crear"),
    path("<int:id_turno>/modificar", views.ModificarTurno, name="modificarturno"),
    path("<int:id_turno>/eliminar", views.EliminarTurno, name="eliminarturno"),
    path("<int:id_turno>/alternaratendido", views.AlternarAtendido, name="alternaratendido"),
]