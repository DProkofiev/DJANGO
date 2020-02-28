from django.urls import path
from firstsiteapp import views
from .views import BookList
from django.conf.urls import url


app_name = 'firstsiteapp'

urlpatterns = [
    path('', BookList.as_view(),  name='index'),
   # path('', views.main_view, name='index'),
    path('create/', views.create_book, name='create'),
    path('book/<int:id>/', views.book, name='book')
    ]