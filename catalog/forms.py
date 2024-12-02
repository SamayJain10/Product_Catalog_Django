from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    category = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'category']
