from django.db import models

# Create your models here.


class Bottle(models.Model):
    height = models.DecimalField()
    width = models.DecimalField()
    length = models.DecimalField()


class AquaBottle(models.Model):
    bootle = models.ForeignKey(Bottle, on_delete=models.CASCADE)
    volume = models.DecimalField()
