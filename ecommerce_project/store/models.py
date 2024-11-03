from autoslug import AutoSlugField
from django.core.validators import MinValueValidator
from django.db import models
from versatileimagefield.fields import VersatileImageField

from .managers import CategoryManager, ProductManager, ProductTagManager


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name", unique=True)
    description = models.TextField(blank=True)
    parent = models.ForeignKey(
        "self", related_name="+", null=True, on_delete=models.SET_NULL, blank=True
    )
    image = VersatileImageField(upload_to="categories/", null=True, blank=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name


class ProductTag(models.Model):
    name = models.CharField(max_length=50)
    objects = ProductTagManager()


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name", unique=True)
    description = models.TextField(blank=True)
    image = VersatileImageField(upload_to="products/", null=True, blank=True)
    price = models.FloatField(validators=[MinValueValidator(0)])
    category = models.ManyToManyField(Category)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    tag = models.ManyToManyField(ProductTag, related_name="tags")

    objects = ProductManager()

    def __str__(self):
        return self.name
