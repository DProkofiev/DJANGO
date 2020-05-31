from django import forms
from .models import Book

class BookForm(forms.Form):
    name = forms.CharField(label='Название книги',
                           widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    authors = forms.CharField(label='Автор(ы)')
    language = forms.CharField(label='Язык')
    link = forms.URLField(label='Ссылка')

    class Meta:
        model = Book
        exclude = ('user',)
