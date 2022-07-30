from django.db import models

# Create your models here.


class BoilerAuth(models.Model):
    keytoken = models.CharField(max_length=255, unique=True)
