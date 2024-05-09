from webapp.models import Product, Category
from django import forms


class ProductForm(forms.ModelForm):
    remaining_quantity = forms.IntegerField(min_value=0)

    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
