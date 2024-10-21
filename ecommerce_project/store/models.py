from django.core.validators import MinValueValidator
from django.db import models

from .managers import CategoryManager, ProductManager


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    parent = models.ForeignKey(
        "self", related_name="+", null=True, on_delete=models.SET_NULL, blank=True
    )

    objects = CategoryManager()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    price = models.FloatField(validators=[MinValueValidator(0)])
    category = models.ManyToManyField(Category)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])

    objects = ProductManager()

    def __str__(self):
        return self.name
