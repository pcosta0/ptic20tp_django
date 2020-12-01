from django.urls import path
from . import views

app_name = 'gerencia'

urlpatterns = [
    path("", views.Informes, name="informes"),
    path("informes/<int:num_informe>", views.Informe, name="informe"),
]