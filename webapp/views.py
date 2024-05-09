from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Category, Product
from webapp.forms import ProductForm, CategoryForm


def home(request):
    products = Product.objects.all()
    return render(request, 'products_view.html', {'products': products})


def detail(request, *args, pk, **kwargs):
    products = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', {'products': products})


def add_category(request):
    if request.method == 'GET':
        form = CategoryForm()
        return render(request, 'category_add_view.html', {'form': form})
    elif request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            Category.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
            )
            return redirect('home')
        else:
            return render(request, 'category_add_view.html', {'form': form})


def add_product(request):
    if request.method == 'GET':
        form = ProductForm()
        category = Category.objects.all()
        return render(request, 'product_add_view.html', {'form': form, 'category': category})
    elif request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            category_id = form.cleaned_data.get('category').id
            category = Category.objects.get(id=category_id)
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                cost=form.cleaned_data.get('cost'),
                category=category,
                imagine=form.cleaned_data.get('imagine'),
            )
            return redirect('home')
        else:
            return render(request, 'product_add_view.html', {'form': form})
