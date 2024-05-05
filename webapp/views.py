from django.shortcuts import render, get_object_or_404
from webapp.models import Category, Product


def home(request):
    products = Product.objects.all()
    return render(request, 'products_view.html', {'products': products})


def detail(request, *args, pk, **kwargs):
    products = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', {'products': products})
