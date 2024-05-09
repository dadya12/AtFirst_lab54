from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование', unique=True)
    description = models.TextField(max_length=500, verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(max_length=500, verbose_name='Описание', blank=True, null=True)
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    category = models.ForeignKey('webapp.Category', on_delete=models.CASCADE, verbose_name='Категория',
                                 related_name='cat', null=True)
    cost = models.DecimalField(verbose_name='Стоимость', max_digits=7, decimal_places=2)
    remaining_quantity = models.IntegerField(verbose_name='Остаток', default=0, validators=[MinValueValidator(0)], help_text='Не может быть ниже 0')
    imagine = models.CharField(verbose_name='Изображение', max_length=500)
