from modeltranslation.translator import TranslationOptions, register

from .models import CustomUser


@register(CustomUser)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        "first_name",
        "last_name",
    )
