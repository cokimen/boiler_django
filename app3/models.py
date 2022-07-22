from django.db import models

# Create your models here.


class PersonSample(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=400)
    birth_date = models.DateField()


class SchoolSample(models.Model):
    school_name = models.CharField(max_length=50)
    person = models.ForeignKey(PersonSample,  on_delete=models.CASCADE)

    SD = 'SD'
    SMP = 'SMP'
    SMA = 'SMA'
    KULIAH = 'KULIAH'

    SCHOOL_CHOICES = [
        (SD, 'SD'),
        (SMP, 'SLTP Bro'),
        (SMA, 'SMA'),
        (KULIAH, 'Kuliah BSI Aja')
    ]
    school_level = models.CharField(
        max_length=50,
        choices=SCHOOL_CHOICES,
        default=SD,
    )
