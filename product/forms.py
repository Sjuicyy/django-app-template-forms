from dataclasses import fields
from django import forms

from .models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'title',
            'description',
            'price',
        ]
        
        
        
class RawProductForm(forms.Form):
     title          = forms.CharField()
     description    = forms.CharField()
     price          = forms.DecimalField()
