from django.db import models

# Create your models here.


class Train(models.Model):
    manufacture_name = models.CharField(max_length=50)
    country_manufacture = models.CharField(max_length=50)

    @property
    def set_country_manufacture(self):
        return "id"
