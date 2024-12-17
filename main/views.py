from django.shortcuts import render
from django.db.models import Avg

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
