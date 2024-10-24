from django.db.models import F
from django.shortcuts import render, redirect

from store.models import Product
from .models import Cart, CartItem


def cart(request):
    if request.method == 'POST' and 'delete_item_id' in request.POST:
        CartItem.objects.delete(request.POST.get('delete_item_id'))

    # if request.user.is_authenticated:
    user_id = request.user.id
    items = CartItem.objects.get_cart_items(user_id)

    context = {
        "items": items
    }

    return render(request, "cart.html", context)


def add_item_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        p = Product.objects.get(id=product_id)
        user_cart = Cart.objects.get(user=request.user.id)

        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=p)

        if not created:
            if cart_item.quantity < cart_item.product.quantity:
                cart_item.quantity += 1
        else:
            cart_item.quantity = 1
        cart_item.save()

        return redirect(request.META.get('HTTP_REFERER', '/'))


def order_checkout(request):
    return render(request, "checkout.html")
