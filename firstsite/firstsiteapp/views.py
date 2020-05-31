
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Book, Category, Year
from django.urls import reverse, reverse_lazy
from .forms import BookForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin


def main_view(request):
    books = Book.objects.all()[:15]
    return render(request, 'firstsiteapp/index.html', context={'books': books})



def create_book(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'firstsiteapp/create.html', context={'form': form})
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            link = form.cleaned_data['link']
            return HttpResponseRedirect(reverse('firstsite:index'))
        else:
             return render(request, 'firstsiteapp/create.html', context={'form': form})


def book(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'firstsiteapp/book.html', context={'book': book})

@user_passes_test(lambda u: u.is_superuser)
def db(request):
    return render(request, 'firstsiteapp/db.html')


class BookList(ListView):
    model = Book
    paginate_by = 10



class NameContextMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)
        return context


class CatListView(ListView, NameContextMixin):
    model = Category
    template_name = 'firstsiteapp/cat_list.html'
    context_object_name = 'categories'

    def get_queryset(self):

        return Category.objects.all()


class CatCreateView(CreateView, NameContextMixin):
    fields = '__all__'
    model = Category
    success_url = reverse_lazy('firstsite:cat_list')
    template_name = 'firstsiteapp/cat_create.html'

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)


class CatEditView(UpdateView):
    fields = '__all__'
    model = Category
    success_url = reverse_lazy('firstsite:cat_list')
    template_name = 'firstsiteapp/cat_create.html'


class CatDeleteView(DeleteView):
    template_name = 'firstsiteapp/cat_delete.html'
    model = Category
    success_url = reverse_lazy('firstsite:cat_list')


class CatListView(ListView, NameContextMixin):
    model = Category
    template_name = 'firstsiteapp/cat_list.html'
    context_object_name = 'categories'

    def get_queryset(self):

        return Category.objects.all()


class YearCreateView(CreateView, NameContextMixin):
    fields = '__all__'
    model = Year
    success_url = reverse_lazy('firstsite:year_list')
    template_name = 'firstsiteapp/year_create.html'

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)


class YearEditView(UpdateView):
    fields = '__all__'
    model = Year
    success_url = reverse_lazy('firstsite:year_list')
    template_name = 'firstsiteapp/year_create.html'


class YearDeleteView(DeleteView):
    template_name = 'firstsiteapp/year_delete.html'
    model = Year
    success_url = reverse_lazy('firstsite:year_list')


class YearListView(ListView, NameContextMixin):
    model = Year
    template_name = 'firstsiteapp/year_list.html'
    context_object_name = 'years'

    def get_queryset(self):
        return Year.objects.all().order_by('-name')