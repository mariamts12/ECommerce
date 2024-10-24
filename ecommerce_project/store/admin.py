from django.contrib import admin

from .models import Category, Product, ProductTag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "parent")
    list_select_related = ("parent",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity")
    search_fields = ("name",)
    ordering = ("price",)


@admin.register(ProductTag)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
