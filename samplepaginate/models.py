from django.db import models

# Create your models here.


class Drink(models.Model):
    name = models.CharField(max_length=90)
    volumne = models.PositiveIntegerField()
