from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
    path("", views.listado, name="listado"),
    path("crear/", views.CrearPaciente, name="crear"),
    path("<int:id_paciente>/modificar", views.ModificarPaciente, name="modificarpaciente"),
    path("<int:id_paciente>/eliminar", views.EliminarPaciente, name="eliminarpaciente"),
    # path("<int:id_paciente>/", views.paciente, name="paciente"),
]