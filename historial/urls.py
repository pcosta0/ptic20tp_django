from django.urls import path
from . import views

app_name = 'historial'

urlpatterns = [
    path("", views.Listado, name="listado"),
    path("<int:id_paciente>", views.HistorialPaciente, name="historialpaciente"),
    path("<int:id_paciente>/crear", views.CrearObservacion, name="crearobservacion"),
    path("modificarobservacion/<int:id_observacion>", views.ModificarObservacion, name="modificarobservacion"),
    path("eliminarobservacion/<int:id_observacion>", views.EliminarObservacion, name="eliminarobservacion"),
]