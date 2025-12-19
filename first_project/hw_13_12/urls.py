from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('history/', views.history),
    path('cities/', views.cities),
    path('facts/', views.facts),

    path('cities/<str:city>/', views.city_detail),
    path('cities/<str:city>/<int:year>/', views.city_year),

    path('history/<int:year>/', views.history_year),
]
