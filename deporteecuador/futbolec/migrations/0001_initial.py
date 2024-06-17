# Generated by Django 5.0.6 on 2024-06-17 19:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('auspiciante', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EquipoFutbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('siglas', models.CharField(max_length=10)),
                ('username_twitter', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CampeonatoEquipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.PositiveIntegerField()),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futbolec.campeonato')),
                ('equipo_futbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futbolec.equipofutbol')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('posicion_campo', models.CharField(choices=[('arquero', 'Arquero'), ('defensa', 'Defensa'), ('centro', 'Centro'), ('delantero', 'Delantero')], max_length=20)),
                ('numero_camiseta', models.PositiveIntegerField()),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('equipo_futbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futbolec.equipofutbol')),
            ],
        ),
    ]
