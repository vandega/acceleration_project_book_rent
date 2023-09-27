from django.db import models


class Condition(models.Model):
    condition = models.CharField(max_length=50, unique=True, blank=False, null=False)

    def __str__(self):
        return f"{self.condition}"


class Genre(models.Model):
    genre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.genre}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    b_day = models.DateField()
    image = models.ImageField(upload_to='images/authors', null=True)

    def __str__(self):
        return f"{self.first_name[0].upper()}. {self.last_name}"


class Book(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    description = models.TextField(verbose_name='description', null=True)
    pages = models.IntegerField(verbose_name='Pages')
    author = models.ManyToManyField(Author, related_name="books")
    genre = models.ManyToManyField(Genre, related_name="books")
    condition = models.ManyToManyField(Condition, related_name="books")
    image = models.ImageField(upload_to='images/books')

    def __str__(self):
        return f"{self.title}"

