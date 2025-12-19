from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_en),
    path('fr/', views.song_fr),
    path('de/', views.song_de),
    path('es/', views.song_es),

    path('cars/', views.cars_home),
    path('toyota/', views.toyota),
    path('honda/', views.honda),
    path('renault/', views.renault),

    path('day/', views.day_of_week),
    path('headphones/', views.headphones),
]
