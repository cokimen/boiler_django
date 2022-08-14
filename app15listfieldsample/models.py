from audioop import maxpp
from django.db import models

# Create your models here.


class Bird(models.Model):
    year_found = models.IntegerField()
    species_name = models.CharField(max_length=100)


class Pigeon(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    CHOICES_SEX = [
        (MALE, 'Laki Laki'),
        (FEMALE, 'Perempuan'),
    ]
    bird = models.ForeignKey('Bird', on_delete=models.CASCADE)
    sex = models.CharField(choices=CHOICES_SEX,
                           blank=True, null=True, max_length=20)
