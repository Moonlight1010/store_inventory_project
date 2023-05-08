from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Stationary','Stationary'),
    ('Electronics','Electronics'),
    ('Food Items', 'Food Items'),
)

class Products(models.Model):
    product_name = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY, blank=True)
    quantity = models.PositiveIntegerField(blank=True)
    unit_price = models.PositiveIntegerField(blank=True)
    total_price = models.PositiveIntegerField(blank=True)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')


class ProductList(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY)
    unit_price = models.PositiveIntegerField()
    quantity_supplied = models.PositiveIntegerField()
    supply_date = models.DateTimeField(auto_now=True)

