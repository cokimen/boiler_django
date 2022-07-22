from django.db import models

# Create your models here.


class Game(models.Model):
    model_name = models.CharField(max_length=50, unique=True)
    model_desc = models.CharField(max_length=100)


class GameDetail(models.Model):
    publisher_name = models.CharField(max_length=10)
    game = models.OneToOneField(
        Game,
        on_delete=models.CASCADE
    )
