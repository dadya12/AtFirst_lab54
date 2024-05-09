from django.urls import path
from webapp.views import home, detail, add_category, add_product, update_product, delete_product

urlpatterns = [
    path('', home, name='home'),
    path('products/', home, name='home_oke'),
    path('products/<int:pk>/', detail, name='detail'),
    path('categories/add/', add_category, name='add_category'),
    path('/products/add/', add_product, name='add_product'),
    path('products/<int:pk>/update/', update_product, name='update_product'),
    path('products/<int:pk>/delete/', delete_product, name='delete_product')
]
