# Generated by Django 4.1 on 2022-10-31 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bouldering', '0003_alter_boulderfinder_finder_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bouldersafety',
            name='safety_grade',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
    ]
