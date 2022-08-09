from django.db import models

# Create your models here.


class Tree(models.Model):
    ordo = models.CharField(max_length=10)
    genus = models.CharField(max_length=10)
