from django.db import models

# Create your models here.


class Author(models.Model):
    author_name = models.CharField(max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
