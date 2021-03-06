# Generated by Django 3.1.3 on 2020-11-27 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_auto_20201126_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.IntegerField(choices=[(0, 'pendiente'), (1, 'pedido'), (2, 'taller')], default=1),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='tipopago',
            field=models.IntegerField(choices=[(0, 'tarjeta de credito'), (1, 'tarjeta de debito'), (2, 'villetera virtual'), (3, 'efectivo')], default=1),
        ),
    ]
