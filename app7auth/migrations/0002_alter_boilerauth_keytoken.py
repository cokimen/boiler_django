# Generated by Django 3.2.12 on 2022-07-30 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app7auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boilerauth',
            name='keytoken',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
