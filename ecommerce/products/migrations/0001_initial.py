# Generated by Django 4.1.4 on 2022-12-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField(default=0)),
                ('ProductCategory', models.CharField(choices=[('Jacket and Sweater', 'Jacket and Sweater'), ('Tops', 'Tops'), ('T-shirt', 'T-shirt'), ('Pants', 'Pants')], default='', max_length=40)),
                ('description', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('image', models.ImageField(upload_to='static/img/')),
            ],
        ),
    ]
