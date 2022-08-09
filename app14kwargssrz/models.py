from django.db import models

# Create your models here.


class Handphone(models.Model):
    name = models.CharField(max_length=40)
    manufacture = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
