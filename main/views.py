from django.http import HttpResponse
from django.shortcuts import render

from main.models import Anime, Genero


def cargar_base_de_datos(request):

    Anime.objects.all().delete()
    Genero.objects.all().delete()
    with open('main/data/animeRS_Dataset/anime.csv') as anime_file:
        anime_file.readline()
        for line in anime_file:
            print(line)
            values = line.split(';')
            anime = Anime.objects.create(
                animeId=int(values[0]),
                titulo=values[1],
                formatoEmision=values[3],
                numEpisodios= int(values[4]) if values[4].isdigit() else 0 #TODO
            )

            generos = values[2].split(',')
            for genero_str in generos:
                try:
                    genero = Genero.objects.get(nombre=genero_str)
                except Genero.DoesNotExist:
                    genero = Genero.objects.create(
                        nombre = genero_str
                    )
                anime.generos.add(genero)

    return HttpResponse('Cargados')