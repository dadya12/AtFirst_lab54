from django.shortcuts import render
from webapp.models import Category, Product


def home(request):
    products = Product.objects.all()
    return render(request, 'products_view.html', {'products': products})
