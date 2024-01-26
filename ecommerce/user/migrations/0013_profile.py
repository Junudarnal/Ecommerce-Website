# Generated by Django 4.1.4 on 2023-01-30 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_cart_added_to_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='profileicon.jpg', upload_to='profile_pics')),
                ('contact', models.PositiveBigIntegerField()),
            ],
        ),
    ]
