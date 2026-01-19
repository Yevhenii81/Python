from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hw_13_01_home'),

    # Задание 1
    path('fortune/', views.fortune, name='fortune'),

    # Задание 2
    path('random/', views.random_number, name='random_number'),
    path('random/<int:min_value>/<int:max_value>/', views.random_number_range, name='random_number_range'),
    path('random_set/<int:count>/', views.random_number_set, name='random_number_set'),

    # Задание 3
    path('poem/random/', views.poem_random, name='poem_random'),
    path('poem/author/<int:author_id>/', views.poem_by_author, name='poem_by_author'),
    path('poem/theme/<int:theme_id>/', views.poem_by_theme, name='poem_by_theme'),

    # Задание 4
    path('authors/', views.all_authors, name='all_authors'),
    path('themes/', views.all_themes, name='all_themes'),
    path('poem_titles/theme/<int:theme_id>/', views.poem_titles_by_theme, name='poem_titles_by_theme'),
    path('poem_titles/author/<int:author_id>/', views.poem_titles_by_author, name='poem_titles_by_author'),
]
