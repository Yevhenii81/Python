from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home),

    path('news/', views.news),
    re_path(r'^news/.+$', views.news),

    path('datetime/', views.current_datetime),
    path('table/', views.multiplication_table),
    path('programmer-day/', views.programmers_day),
]
