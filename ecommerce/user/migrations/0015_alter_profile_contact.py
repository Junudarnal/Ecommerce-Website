# Generated by Django 4.1.4 on 2023-01-31 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.PositiveBigIntegerField(max_length=10),
        ),
    ]
