# Generated by Django 4.1.4 on 2023-01-26 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_remove_order_cart_alter_order_order_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='added_to_order',
            field=models.BooleanField(default=False),
        ),
    ]
