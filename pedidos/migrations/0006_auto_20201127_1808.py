# Generated by Django 3.1.3 on 2020-11-27 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0005_auto_20201127_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fechahora',
            field=models.DateField(),
        ),
    ]
