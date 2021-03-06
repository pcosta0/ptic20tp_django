# Generated by Django 3.1.3 on 2020-11-25 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20201125_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='fecha',
            new_name='fechahora',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.IntegerField(choices=[(1, 'pendiente1'), (2, 'taller2'), (3, 'nose3')], default=1),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='tipopago',
            field=models.IntegerField(choices=[(2, 'tarjeta'), (1, 'efectivo'), (3, 'cheque')], default=1),
        ),
    ]
