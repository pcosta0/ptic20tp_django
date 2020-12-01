# Generated by Django 3.1.3 on 2020-11-12 20:45
from __future__ import unicode_literals
from django.db import migrations, models
from django.contrib.auth.models import User, Group
from pacientes.models import *
from productos.models import *
import os

def forward_func(apps, schema_editor):
    # crea algunos grupos y miembros
    grupo, created = Group.objects.get_or_create(name='gerencia')
    usuario = User.objects.create_user('zeus', 'gerente@clinica.test', 'zeus')
    usuario.first_name = 'zeus'
    usuario.last_name = 'del Olimpo'
    usuario.save()
    usuario.groups.add(grupo)

    grupo, created = Group.objects.get_or_create(name='taller')
    usuario = User.objects.create_user('mario', 'tecnico@clinica.test', 'mario')
    usuario.first_name = 'mario'
    usuario.last_name = 'mario'
    usuario.save()
    usuario.groups.add(grupo)
    
    grupo, created = Group.objects.get_or_create(name='ventas')
    usuario = User.objects.create_user('marykay', 'vendedor@clinica.test', 'marykay')
    usuario.first_name = 'mary kay'
    usuario.last_name = 'ash'
    usuario.save()
    usuario.groups.add(grupo)
    
    grupo, created = Group.objects.get_or_create(name='secretaria')
    usuario = User.objects.create_user('jkrowling', 'secre@clinica.test', 'jkrowling')
    usuario.first_name = 'joanne'
    usuario.last_name = 'rowling'
    usuario.save()
    usuario.groups.add(grupo)
    
    grupo, created = Group.objects.get_or_create(name='profesional')
    usuario = User.objects.create_user('hermioneg', 'medico@clinica.test', 'hermioneg')
    usuario.first_name = 'hermione'
    usuario.last_name = 'granger'
    usuario.save()
    usuario.groups.add(grupo)
    
    usuario = User.objects.create_user('harryp', 'medico@clinica.test', 'harryp')
    usuario.first_name = 'harry'
    usuario.last_name = 'potter'
    usuario.save()
    usuario.groups.add(grupo)
    
    usuario = User.objects.create_user('rweasley', 'medico@clinica.test', 'rweasley')
    usuario.first_name = 'ron'
    usuario.last_name = 'weasley'
    usuario.save()
    usuario.groups.add(grupo)
    
    usuario = User.objects.create_superuser('super', 'super@clinica.test', 'super')
    usuario.first_name = 'Kal'
    usuario.last_name = 'El'
    usuario.save()

    # crea algunos pacientes
    paciente = Paciente(apellido='Muscaria', nombre='Amanita', dni='11111111', activo=True)
    paciente.save()
    paciente = Paciente(apellido='Granulatus', nombre='Suillus', dni='22222222', activo=True)
    paciente.save()
    paciente = Paciente(apellido='Molibdites', nombre='Clorofilum', dni='33333333', activo=True)
    paciente.save()
    paciente = Paciente(apellido='Cubensis', nombre='Psyloscibe', dni='44444444', activo=True)
    paciente.save()
    paciente = Paciente(apellido='Ostreatus', nombre='Pleurotus', dni='55555555', activo=True)
    paciente.save()

    # crea algunos productos
    producto = Producto(nombre='marco plastico', opcion='transparente, opaco, verde, azul, rojo', precio=300, activo=True)
    producto.save()
    producto = Producto(nombre='marco metalico', opcion='plateado, dorado', precio=700, activo=True)
    producto.save()
    producto = Producto(nombre='lente', opcion='lejos, cerca. izquierda, derecha. incluye armazon, no incluye armazon', precio=790, activo=True)
    producto.save()
    producto = Producto(nombre='estuche plastico', opcion='negro, gris, blanco', precio=230, activo=True)
    producto.save()
    producto = Producto(nombre='lente decorativo', opcion='derecho, izquierdo. redondo, ovalado, rectangular. con filtro, sin filtro. antireflejo, sin antireflejo', precio=890, activo=True)
    producto.save()

def reversed_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(forward_func, reversed_func),
    ]
