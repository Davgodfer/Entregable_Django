from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Ocupacion(models.Model):
    ocupacionId = models.AutoField(primary_key=True)
    nombre = models.TextField(verbose_name='Ocupación', unique=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ('nombre', )

class Usuario(models.Model):
    idUsuario = models.TextField(primary_key=True)
    edad = models.IntegerField(verbose_name='Edad', help_text='Debe introducir una edad')
    sexo = models.CharField(max_length=1, verbose_name='Sexo', help_text='Debe elegir entre M o F')
    ocupacion = models.ForeignKey(Ocupacion, on_delete=models.SET_NULL, null=True)
    codigoPostal = models.TextField(verbose_name='Código Postal')

    def __str__(self):
        return self.idUsuario
    
    class Meta:
        ordering = ('idUsuario', )

class Genero(models.Model):
    nombre = models.TextField(verbose_name='Genero')

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering =('nombre', )

class Anime(models.Model):
    animeId = models.IntegerField(primary_key=True)
    titulo = models.TextField(verbose_name='Titulo')
    generos = models.ManyToManyField(Genero)
    formatoEmision = models.TextField(verbose_name = 'Formato de emision')
    numEpisodios = models.IntegerField(verbose_name= 'Numero de episodios')

    def __str__(self):
        return (str(self.titulo))
    
    class Meta:
        ordering = ('titulo', )

class Puntuacion(models.Model):
    idUsuario = models.IntegerField()
    animeId = models.ForeignKey(Anime,on_delete=models.CASCADE)
    puntuacion = models.IntegerField(verbose_name='Puntuación', validators=[MinValueValidator(1), MaxValueValidator(10)])
    
    def __str__(self):
        return (str(self.puntuacion))
    
    class Meta:
        ordering=('animeId','idUsuario', )
    
