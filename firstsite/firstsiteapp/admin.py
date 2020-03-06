from django.contrib import admin

from .models import  Book, Year, Category

admin.site.register(Book)
admin.site.register(Year)
admin.site.register(Category)

"""
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'authors', 'year','category', 'language')
    list_filter = ('name', 'authors', 'language', 'category', 'year')
    search_fields = ('name', 'years', 'category')
    prepopulated_fields = {'link': ('name',)}
    raw_id_fields = ('authors',)
"""