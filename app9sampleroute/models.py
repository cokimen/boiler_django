from django.db import models

# Create your models here.


class CocaCola(models.Model):
    volume = models.IntegerField()
    series = models.CharField(
        max_length=100, unique=True, blank=False, null=False)
