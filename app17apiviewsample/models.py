from django.db import models

# Create your models here.


class Clothes(models.Model):
    brand_name = models.CharField(max_length=100)
