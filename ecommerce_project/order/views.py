from django.shortcuts import render

from .models import Cart


def order_cart(request):
    # if request.user.is_authenticated:
    user_id = request.user.id
    cart = Cart.objects.prefetch_related('items').get(pk=user_id)

    context = {
        "cart": cart
    }
    return render(request, "cart.html", context)


def order_checkout(request):
    return render(request, "checkout.html")
