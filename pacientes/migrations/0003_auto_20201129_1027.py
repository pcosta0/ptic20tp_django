# Generated by Django 3.1.3 on 2020-11-29 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_paciente_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='dni',
            field=models.CharField(max_length=10, verbose_name='dni del paciente'),
        ),
    ]
