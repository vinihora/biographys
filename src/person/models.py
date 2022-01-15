from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    years = models.IntegerField()
    born = models.CharField(max_length=100)
    died = models.CharField(blank=True, max_length=100)
    update = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_books(self):
        return self.books.filter(author = self.name)

    def get_sum_born_died(self):
        born = self.born
        died = self.died
        c = born + died
        return c
        
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    date_of_publication = models.CharField(max_length=100)
    publishing_company = models.CharField(max_length=150)

    def __str__(self):
        return self.name


    