from django.db import models


class Book(models.Model):
    header = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.header} | {self.author} | {self.genre} | {self.publication_year}'
