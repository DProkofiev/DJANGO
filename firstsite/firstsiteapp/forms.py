from django import forms

class BookForm(forms.Form):
    name = forms.CharField(label='Название книги')
    authors = forms.CharField(label='Автор(ы)')
    language = forms.CharField(label='Язык')
    link = forms.URLField(label='Ссылка')


