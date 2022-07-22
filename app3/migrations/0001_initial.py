# Generated by Django 3.2.12 on 2022-07-22 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=400)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SchoolSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=50)),
                ('school_level', models.CharField(choices=[('SD', 'SD'), ('SMP', 'SLTP Bro'), ('SMA', 'SMA'), ('KULIAH', 'Kuliah BSI Aja')], default='SD', max_length=50)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app3.personsample')),
            ],
        ),
    ]
