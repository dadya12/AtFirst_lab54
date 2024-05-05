from django.urls import path
from webapp.views import home, detail

urlpatterns = [
    path('', home, name='home'),
    path('products/', home, name='home_oke'),
    path('products/<int:pk>/', detail, name='detail'),
]
