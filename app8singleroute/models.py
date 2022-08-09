from django.db import models

# Create your models here.


class Car(models.Model):
    brand_name = models.CharField(max_length=50)


class Carburator(models.Model):
    car = models.OneToOneField('Car', on_delete=models.DO_NOTHING)
    manufacture_name = models.CharField(max_length=50)
