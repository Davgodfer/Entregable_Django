# Generated by Django 5.1.2 on 2024-12-17 12:59

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idGenero', models.TextField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(verbose_name='Genero')),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('ocupacionId', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(unique=True, verbose_name='Ocupación')),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('animeId', models.TextField(primary_key=True, serialize=False)),
                ('titulo', models.TextField(verbose_name='Titulo')),
                ('formatoEmision', models.TextField(verbose_name='Formato de emision')),
                ('numEpisodios', models.IntegerField(verbose_name='Numero de episodios')),
                ('generos', models.ManyToManyField(to='main.genero')),
            ],
            options={
                'ordering': ('titulo',),
            },
        ),
        migrations.CreateModel(
            name='Puntuacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUsuario', models.IntegerField()),
                ('puntuacion', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Puntuación')),
                ('animeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.anime')),
            ],
            options={
                'ordering': ('animeId', 'idUsuario'),
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.TextField(primary_key=True, serialize=False)),
                ('edad', models.IntegerField(help_text='Debe introducir una edad', verbose_name='Edad')),
                ('sexo', models.CharField(help_text='Debe elegir entre M o F', max_length=1, verbose_name='Sexo')),
                ('codigoPostal', models.TextField(verbose_name='Código Postal')),
                ('ocupacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.ocupacion')),
            ],
            options={
                'ordering': ('idUsuario',),
            },
        ),
    ]