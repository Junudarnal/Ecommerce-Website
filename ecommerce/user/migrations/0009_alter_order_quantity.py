# Generated by Django 4.1.4 on 2023-01-22 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_order_subtotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]