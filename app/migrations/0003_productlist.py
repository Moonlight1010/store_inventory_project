# Generated by Django 3.2 on 2022-10-04 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_products_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Stationary', 'Stationary'), ('Electronics', 'Electronics'), ('Food Items', 'Food Items')], max_length=100)),
                ('unit_price', models.PositiveIntegerField()),
                ('quantity_supplied', models.PositiveIntegerField()),
                ('supply_date', models.PositiveIntegerField()),
            ],
        ),
    ]
