from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Avg
from main.models import Anime, Genero, Puntuacion

def menu_principal(request):
    return render(request, 'menu_principal.html')

def animes_por_genero(request):
    if request.method == 'POST':
        genero = request.POST['genero']
        animes = Anime.objects.filter(generos__nombre=genero)
        return render(request, 'animes_por_genero.html', {'animes': animes, 'genero': genero})

    generos = Genero.objects.values_list('nombre', flat=True).distinct()
    return render(request, 'animes_por_genero_form.html', {'generos': generos})

def mejores_animes(request):
    animes = Anime.objects.annotate(puntuacion_media=Avg('puntuacion__puntuacion')).order_by('-puntuacion_media')[:3]
    return render(request, 'mejores_animes.html', {'animes': animes})

def cargar_base_datos(request):

    Anime.objects.all().delete()
    Genero.objects.all().delete()
    with open('main/data/animeRS_Dataset/anime.csv') as anime_file:
        anime_file.readline()
        for line in anime_file:
            values = line.split(';')
            anime = Anime.objects.create(
                animeId=int(values[0]),
                titulo=values[1],
                formatoEmision=values[3],
                numEpisodios= int(values[4]) if values[4].strip().isdigit() else 0 #TODO
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

    Puntuacion.objects.all().delete()
    with open('main/data/animeRS_Dataset/ratings.csv') as puntuacion_file:
        puntuacion_file.readline()
        for line in puntuacion_file:
            values = line.split(';')
            anime = Puntuacion.objects.create(
                idUsuario = int(values[0]),
                anime_id = int(values[1]),
                puntuacion = int(values[2])
            )

    return HttpResponse('Cargados')