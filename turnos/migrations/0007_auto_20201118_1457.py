# Generated by Django 3.1.3 on 2020-11-18 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0006_auto_20201118_1456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='turno',
            options={'get_latest_by': 'fecha', 'ordering': ['-fecha']},
        ),
    ]
