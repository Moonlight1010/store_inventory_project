from .models import Products, ProductList
from django import forms

class ProductForm(forms.ModelForm):
    class Meta():
        model = Products
        fields = ('product_name', 'category', 'quantity', 'unit_price')

class ProductListForm(forms.ModelForm):
    class Meta():
        model = ProductList
        fields = ('product_name', 'category', 'unit_price', 'quantity_supplied')
