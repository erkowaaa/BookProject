from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    pages = models.IntegerField(default=0)
    image = models.ImageField(upload_to='img/')
    have = models.BooleanField(default=True)

    def __str__(self):
        return self.title

