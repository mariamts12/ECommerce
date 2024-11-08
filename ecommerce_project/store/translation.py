from modeltranslation.translator import TranslationOptions, register

from .models import Category, Product, ProductTag


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "description",
    )


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "description",
    )


@register(ProductTag)
class TagTranslationOptions(TranslationOptions):
    fields = ("name",)
