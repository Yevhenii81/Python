from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_home, name='library_home'),

    path('books/', views.book_list, name='book_list'),
    path('books/available/', views.book_available_list, name='book_available'),
    path('books/add/', views.book_create, name='book_create'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/<int:book_id>/edit/', views.book_update, name='book_update'),
    path('books/<int:book_id>/delete/', views.book_delete, name='book_delete'),

    path('readers/', views.reader_list, name='reader_list'),
    path('readers/add/', views.reader_create, name='reader_create'),
    path('readers/<int:reader_id>/', views.reader_detail, name='reader_detail'),
    path('readers/<int:reader_id>/edit/', views.reader_update, name='reader_update'),
    path('readers/<int:reader_id>/delete/', views.reader_delete, name='reader_delete'),
]
