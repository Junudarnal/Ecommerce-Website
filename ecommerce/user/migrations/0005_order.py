# Generated by Django 4.1.4 on 2023-01-12 11:16

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_products_description'),
        ('user', '0004_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200, verbose_name=django.contrib.auth.models.User)),
                ('shipping_address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=10)),
                ('zip', models.CharField(max_length=10)),
                ('quantity', models.PositiveIntegerField()),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subtotal', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('order_status', models.CharField(choices=[('ORDER RECEIVED', 'ORDER RECEIVED'), ('ORDER PROCESSING', 'ORDER PROCESSING'), ('ON THE WAY', 'ON THE WAY'), ('ORDER COMPLETED', 'ORDER COMPLETED'), ('ORDER CANCELED', 'ORDER CANCELED')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.CharField(choices=[('KHALTI', 'KHALTI'), ('CASH ON DELIVERY', 'CASH ON DELIVERY')], default='CASH ON DELIVERY', max_length=20)),
                ('payment_completed', models.BooleanField(blank=True, default=False, null=True)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
    ]