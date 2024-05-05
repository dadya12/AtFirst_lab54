from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Category, Product


def home(request):
    products = Product.objects.all()
    return render(request, 'products_view.html', {'products': products})


def detail(request, *args, pk, **kwargs):
    products = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', {'products': products})


def add_category(request):
    if request.method == 'GET':
        return render(request, 'category_add_view.html')
    elif request.method == "POST":
        category = Category.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
        )
        return redirect('home')
