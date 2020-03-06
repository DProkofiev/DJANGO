from django.db import models

# models.DataField
    # models.DateTimeField
    # models.TimeField
    # models.IntegerField
    # models.PositiveIntegerField
    # models.PositiveSmallIntegerField
    # models.FloatField
    # models.DecimalField
    # models.BooleanField
    # models.BinaryField
    # models.ImageField
    # models.FileField
    # models.URLField
    # models.EmailField


class Year(models.Model):
    name = models.CharField(max_length=4, unique=True)
   # description = models.CharField(max_length=4, unique=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=16, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=32, unique=False)
    description = models.TextField(blank=False)
    link = models.URLField(max_length=128, unique=False)
    authors = models.CharField(max_length=16, unique=False)
    language = models.CharField(max_length=20, unique=False)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CoreObject(models.Model):
    name = models.CharField(max_length=32)