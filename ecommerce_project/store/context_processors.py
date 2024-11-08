from django.core.cache import cache
from django.utils.translation import get_language
from order.models import Cart

from .models import Category


def global_context(request):
    language = get_language()
    cache_key = f"cached_categories_{language}"
    categories = cache.get(cache_key)
    if not categories:
        categories = Category.objects.get_top_categories()
        cache.set(cache_key, categories, 300)

    if request.user.is_authenticated:
        cart_items_quantity = Cart.objects.get_quantity(request.user.id)
    else:
        cart_items_quantity = 0

    return {"header_categories": categories, "cart_items_quantity": cart_items_quantity}
