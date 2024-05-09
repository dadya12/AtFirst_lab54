from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Category, Product
from webapp.forms import ProductForm, CategoryForm
from django.db.models.functions import Lower


def home(request):
    products = Product.objects.all().filter(remaining_quantity__gte=1).order_by('category__title', Lower('title'))
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
                remaining_quantity=form.cleaned_data.get('remaining_quantity'),
                imagine=form.cleaned_data.get('imagine'),
            )
            return redirect('home')
        else:
            return render(request, 'product_add_view.html', {'form': form})


def update_product(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'title': product.title,
            'description': product.description,
            'category': product.category,
            'cost': product.cost,
            'remaining_quantity': product.remaining_quantity,
            'imagine': product.imagine
        })
        return render(request, 'products_update_view.html', {'form': form})
    elif request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.title = form.cleaned_data.get('title')
            product.description = form.cleaned_data.get('description')
            product.category = form.cleaned_data.get('category')
            product.cost = form.cleaned_data.get('cost')
            product.remaining_quantity = form.cleaned_data.get('remaining_quantity')
            product.imagine = form.cleaned_data.get('imagine')
            product.save()
            return redirect('home')
        else:
            product.save()
            return render(request, 'products_update_view.html', {'form': form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_product.html', {'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('home')
