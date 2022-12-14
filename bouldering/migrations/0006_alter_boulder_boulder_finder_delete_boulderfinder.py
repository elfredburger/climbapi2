# Generated by Django 4.1 on 2022-11-06 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bouldering', '0005_alter_bouldergrade_boulder_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boulder',
            name='boulder_finder',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='boulder finder'),
        ),
        migrations.DeleteModel(
            name='BoulderFinder',
        ),
    ]
