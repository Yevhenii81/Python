from django.shortcuts import render, get_object_or_404
from .models import Book, Reader

def library_home(request):
    return render(request, 'hw_18_12/home.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'hw_18_12/book_list.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'hw_18_12/book_detail.html', {'book': book})


def reader_list(request):
    readers = Reader.objects.all()
    return render(request, 'hw_18_12/reader_list.html', {'readers': readers})


def reader_detail(request, reader_id):
    reader = get_object_or_404(Reader, id=reader_id)
    return render(request, 'hw_18_12/reader_detail.html', {'reader': reader})
