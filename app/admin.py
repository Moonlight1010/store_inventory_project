from django.contrib import admin
from .models import Products, ProductList

# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'quantity', 'unit_price', 'total_price')

@admin.register(ProductList)
class ProductListAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'unit_price', 'quantity_supplied', 'supply_date')
    search_fields = ('product_name',)
    list_display_links = ('product_name',)
    list_filter = ('product_name',)
