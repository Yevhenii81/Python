from django import forms
from .models import Book, Reader

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'year',
            'style',
            'publisher',
            'is_available'
        ]


class ReaderForm(forms.ModelForm):
    books = forms.ModelMultipleChoiceField(
        queryset=Book.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Reader
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'register_date',
            'books'
        ]

