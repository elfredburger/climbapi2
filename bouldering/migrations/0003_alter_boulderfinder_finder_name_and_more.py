# Generated by Django 4.1 on 2022-09-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bouldering', '0002_auto_20220901_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boulderfinder',
            name='finder_name',
            field=models.CharField(default=1, max_length=30, unique=True, verbose_name='finder of the route'),
        ),
        migrations.AlterField(
            model_name='bouldergrade',
            name='boulder_grade',
            field=models.CharField(max_length=10, unique=True, verbose_name='grade'),
        ),
        migrations.AlterField(
            model_name='boulderlocation',
            name='location_name',
            field=models.CharField(default=1, max_length=50, unique=True, verbose_name='location name'),
        ),
        migrations.AlterField(
            model_name='bouldersafety',
            name='safety_grade',
            field=models.CharField(default=1, max_length=50, unique=True, verbose_name='safety grade'),
        ),
    ]
