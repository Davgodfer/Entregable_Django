# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_principal, name='menu_principal'),
    path('cargar_base_datos/', views.cargar_base_datos, name='cargar_base_datos'),
    path('mostrar_registros/', views.mostrar_registros, name='mostrar_registros'),
    path('cargar_recsys/', views.cargar_recsys, name='cargar_recsys'),
    path('animes_por_genero/', views.animes_por_genero, name='animes_por_genero'),
    path('mejores_animes/', views.mejores_animes, name='mejores_animes'),
    path('recomendar_animes/', views.recomendar_animes, name='recomendar_animes'),
]