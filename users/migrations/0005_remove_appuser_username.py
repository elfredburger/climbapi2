# Generated by Django 4.1 on 2022-11-06 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_appuser_user_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='username',
        ),
    ]
