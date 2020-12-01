from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.vista_login, name="login"),
    path("logout", views.vista_logout, name="logout")
]