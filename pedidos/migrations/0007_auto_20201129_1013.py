# Generated by Django 3.1.3 on 2020-11-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0006_auto_20201127_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.IntegerField(choices=[(0, 'pendiente'), (1, 'pedido'), (2, 'taller'), (3, 'finalizado')], default=1),
        ),
    ]