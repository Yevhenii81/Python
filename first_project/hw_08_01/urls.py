from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('add/', views.restaurant_create, name='restaurant_create'),
    path('<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('<int:restaurant_id>/edit/', views.restaurant_update, name='restaurant_update'),
    path('<int:restaurant_id>/delete/', views.restaurant_delete, name='restaurant_delete'),
]
