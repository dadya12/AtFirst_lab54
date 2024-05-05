from django.urls import path
from webapp.views import home, detail, add_category

urlpatterns = [
    path('', home, name='home'),
    path('products/', home, name='home_oke'),
    path('products/<int:pk>/', detail, name='detail'),
    path('categories/add/', add_category, name='add_category'),
]
