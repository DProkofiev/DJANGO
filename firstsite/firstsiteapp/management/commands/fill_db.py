
import csv
import sys
from django.core.management.base import BaseCommand
from firstsiteapp.models import Book, Year, Category

DATA_FILENAME = '/Users/dprokofiev/PycharmProjects/knigi/books.csv'
books_list = []

with open(DATA_FILENAME, newline='') as file:
    reader = csv.reader(file)
    try:
        for row in reader:
            books_list.append(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(DATA_FILENAME, reader.line_num, e))


def clear_text(text):
    bad_chars= ["\\t", "  ", "[", "         ", "МБ", "]: ", "Mb", "Формат: PDF", " /???",  " до г."
                '(не нужен)', ' ( не нужен)', "\\", "\\t", ". мб", ' Мб', ", Мб", "\t", ": ", "\\xa0", "0 ", "-0", "0, ",
                 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in bad_chars:
        text = text.replace(char, "")
    return text

class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Year.objects.all().delete()
        Book.objects.all().delete()
        cat_set = set(x[6][1:-1]for x in books_list)
        years_set = set(x[4] for x in books_list)
        for cat in cat_set:
            Category.objects.create(name=cat, description='None')
        for year in years_set:
            Year.objects.create(name=year)
        for book in books_list:
            name = book[0]
            link = book[1]
            authors = clear_text(book[3]) if book[3] is not '' or book[3] is not '.' or book[3] is not '-' else None
            language = clear_text(book[5]) if book[5] is not '' or book[5] is not '.' or book[5] is not '-' else None
            year = book[4]
            category = book[6][1:-1]
            Book.objects.create(name=name,
                                link=link,
                                authors = authors,
                                language=language,
                                year=Year.objects.get(name=year),
                                category=Category.objects.get(name=category))
