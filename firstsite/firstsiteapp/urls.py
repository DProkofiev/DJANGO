from django.urls import path
from firstsiteapp import views


app_name = 'firstsiteapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    ]