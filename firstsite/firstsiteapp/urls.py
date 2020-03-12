from django.urls import path
from firstsiteapp import views
from .views import BookList
from django.conf.urls import url


app_name = 'firstsiteapp'

urlpatterns = [
    path('', BookList.as_view(),  name='index'),
   # path('', views.main_view, name='index'),
    path('create/', views.create_book, name='create_link'),
    path('db/', views.db, name='db_link'),
    path('book/<int:id>/', views.book, name='book'),
    path('cat-list', views.CatListView.as_view(), name='cat_list'),
    path('cat-create/', views.CatCreateView.as_view(), name='cat_create'),
    path('cat-edit/<int:pk>/', views.CatEditView.as_view(), name='cat_edit'),
    path('cat-delete/<int:pk>/', views.CatDeleteView.as_view(), name='cat_delete'),
    path('year-list', views.YearListView.as_view(), name='year_list'),
    path('year-create/', views.YearCreateView.as_view(), name='year_create'),
    path('year-edit/<int:pk>/', views.YearEditView.as_view(), name='year_edit'),
    path('year-delete/<int:pk>/', views.YearDeleteView.as_view(), name='year_delete')
    ]