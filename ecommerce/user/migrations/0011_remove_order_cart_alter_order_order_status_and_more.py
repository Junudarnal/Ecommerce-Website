# Generated by Django 4.1.4 on 2023-01-26 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_remove_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('ORDER PENDING', 'ORDER PENDING'), ('ORDER COMPLETED', 'ORDER COMPLETED')], max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ManyToManyField(blank=True, null=True, to='user.cart'),
        ),
    ]
