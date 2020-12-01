from django.urls import path
from .views import *

app_name = 'paginas'

urlpatterns = [
    path('', vista_inicio, name='inicio'),
    path('acercade/', vista_acercade, name='acercade'),
]
