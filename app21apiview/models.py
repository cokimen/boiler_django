from django.db import models

# Create your models here.


class Cosmos(models.Model):
    galaxy_group = models.CharField(max_length=100)

    class Meta:
        abstract = False
