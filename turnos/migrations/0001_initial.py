# Generated by Django 3.1.3 on 2020-11-15 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.IntegerField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='doctores', to=settings.AUTH_USER_MODEL)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='pacientes', to='pacientes.paciente')),
            ],
        ),
    ]