from django.core.cache import cache
from order.models import Cart

from .models import Category


def global_context(request):
    categories = cache.get("cached_categories")
    if not categories:
        categories = Category.objects.get_top_categories()
        cache.set("cached_categories", categories, 600)

    if request.user.is_authenticated:
        cart_items_quantity = Cart.objects.get_quantity(request.user.id)
    else:
        cart_items_quantity = 0

    return {"header_categories": categories, "cart_items_quantity": cart_items_quantity}
