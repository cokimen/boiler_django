from django.db import models

# Create your models here.


class Ocean(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    color_water = models.CharField(max_length=50)


class Fish(models.Model):
    ocean = models.ForeignKey(Ocean, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


# class Crab(models.Model):
#     pass
