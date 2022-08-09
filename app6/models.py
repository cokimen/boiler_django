from django.db import models

# Create your models here.


class Furniture(models.Model):
    merk = models.CharField(max_length=100)
    dimension = models.DecimalField(decimal_places=4, max_digits=8)
