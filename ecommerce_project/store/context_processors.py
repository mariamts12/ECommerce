from order.models import Cart

from .models import Category


def global_context(request):
    categories = Category.objects.get_top_categories()
    cart_items_quantity = Cart.objects.get_quantity(request.user.id)

    return {"header_categories": categories, "cart_items_quantity": cart_items_quantity}
