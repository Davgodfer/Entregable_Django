"""
URL configuration for practica_tres project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    # path('', views.menu_principal, name='menu_principal'),
    path('cargar_base_datos/', views.cargar_base_datos, name='cargar_base_datos'),
    # path('mostrar_registros/', views.mostrar_registros, name='mostrar_registros'),
    # path('cargar_recsys/', views.cargar_recsys, name='cargar_recsys'),
    path('animes_por_genero/', views.animes_por_genero, name='animes_por_genero'),
    path('mejores_animes/', views.mejores_animes, name='mejores_animes'),
    # path('recomendar_animes/', views.recomendar_animes, name='recomendar_animes'),
]
