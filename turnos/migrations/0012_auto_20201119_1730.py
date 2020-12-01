# Generated by Django 3.1.3 on 2020-11-19 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pacientes', '0002_paciente_activo'),
        ('turnos', '0011_auto_20201118_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='turnodoctores', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='turno',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='turnopacientes', to='pacientes.paciente'),
        ),
    ]