from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book, Reader
from .forms import BookForm, ReaderForm


# ===== ГЛАВНАЯ =====
def library_home(request):
    return render(request, 'hw_18_12/home.html')


# ===== КНИГИ =====
def book_list(request):
    books = Book.objects.all()
    return render(request, 'hw_18_12/book_list.html', {'books': books})


def book_available_list(request):
    books = Book.objects.filter(is_available=True)
    return render(request, 'hw_18_12/book_list.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'hw_18_12/book_detail.html', {'book': book})


@login_required
@permission_required('library.add_book', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'hw_18_12/book_form.html', {'form': form})


@login_required
@permission_required('library.change_book', raise_exception=True)
def book_update(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)

    return render(request, 'hw_18_12/book_form.html', {'form': form})


@login_required
@permission_required('library.delete_book', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'hw_18_12/confirm_delete.html', {'book': book})


# ===== ЧИТАТЕЛИ =====
def reader_list(request):
    readers = Reader.objects.all()
    return render(request, 'hw_18_12/reader_list.html', {'readers': readers})


def reader_detail(request, reader_id):
    reader = get_object_or_404(Reader, id=reader_id)
    return render(request, 'hw_18_12/reader_detail.html', {'reader': reader})


@login_required
@permission_required('library.add_reader', raise_exception=True)
def reader_create(request):
    if request.method == 'POST':
        form = ReaderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reader_list')
    else:
        form = ReaderForm()

    return render(request, 'hw_18_12/reader_form.html', {'form': form})


@login_required
@permission_required('library.change_reader', raise_exception=True)
def reader_update(request, reader_id):
    reader = get_object_or_404(Reader, id=reader_id)

    if request.method == 'POST':
        form = ReaderForm(request.POST, instance=reader)
        if form.is_valid():
            form.save()
            return redirect('reader_detail', reader_id=reader.id)
    else:
        form = ReaderForm(instance=reader)

    return render(request, 'hw_18_12/reader_form.html', {'form': form})


@login_required
@permission_required('library.delete_reader', raise_exception=True)
def reader_delete(request, reader_id):
    reader = get_object_or_404(Reader, id=reader_id)

    if request.method == 'POST':
        reader.delete()
        return redirect('reader_list')

    return render(request, 'hw_18_12/confirm_delete.html', {'reader': reader})
