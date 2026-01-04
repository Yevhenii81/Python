from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('login/', views.login_view),
    path('calc/', views.calc_view),
    path('register/', views.register_view),
    path('programmer-day/', views.programmer_day),
]
