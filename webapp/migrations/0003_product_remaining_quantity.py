# Generated by Django 5.0.4 on 2024-05-09 16:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_product_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='remaining_quantity',
            field=models.IntegerField(default=0, help_text='Не может быть ниже 0', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Остаток'),
        ),
    ]
