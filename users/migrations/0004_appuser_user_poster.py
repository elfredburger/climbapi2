# Generated by Django 4.1 on 2022-11-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_appuser_user_about_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='user_poster',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
