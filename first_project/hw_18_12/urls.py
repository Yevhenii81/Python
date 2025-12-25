from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_home),
    
    path('books/', views.book_list),
    path('books/<int:book_id>/', views.book_detail),

    path('readers/', views.reader_list),
    path('readers/<int:reader_id>/', views.reader_detail),
]
