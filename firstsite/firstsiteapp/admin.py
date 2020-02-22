from django.contrib import admin

from .models import  Book, Year, Category

admin.site.register(Book)
admin.site.register(Year)
admin.site.register(Category)
