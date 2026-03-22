from django import forms
from django.forms import ModelForm, TextInput, Textarea, NumberInput
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'content']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название товара'}),
            'content': Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст описания товара'}),
            'price': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена товара'}),
        }