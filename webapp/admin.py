from django.contrib import admin
from webapp.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_filter = ['id', 'title']
    search_fields = ['title', 'id']
    fields = ['title', 'description']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'add_date', 'category', 'cost']
    list_filter = ['id', 'title']
    search_fields = ['title', 'id']
    fields = ['title', 'description', 'add_date', 'category', 'cost', 'imagine']
    readonly_fields = ['add_date']
