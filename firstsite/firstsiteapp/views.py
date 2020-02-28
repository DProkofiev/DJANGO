from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Book
from django.urls import reverse
from .forms import BookForm
from django.views import generic


def main_view(request):
    books = Book.objects.all()[:15]
    return render(request, 'firstsiteapp/index.html', context={'books': books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            link = form.cleaned_data['link']
            return HttpResponseRedirect(reverse('firstsite:index'))
        else:
            return render(request, 'firstsiteapp/create.html', context={'form': form})
    else:
        form = BookForm()
        return render(request, 'firstsiteapp/create.html', context={'form': form})

def book(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'firstsiteapp/book.html', context={'book': book})

class BookList(generic.ListView):
    model = Book
    paginate_by = 10