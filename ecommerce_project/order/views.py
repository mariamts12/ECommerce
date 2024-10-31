from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DeleteView
from store.models import Product

from .models import Cart, CartItem


@method_decorator(login_required, name="dispatch")
class CartView(View):
    def get(self, request):
        user_id = request.user.id
        items = CartItem.objects.get_cart_items(user_id).prefetch_related("product")

        context = {"items": items}

        return render(request, "cart.html", context)


@method_decorator(login_required, name="dispatch")
class DeleteCartItem(DeleteView):
    model = CartItem
    success_url = reverse_lazy("cart")


@method_decorator(login_required, name="dispatch")
class AddCartItemView(View):
    def post(self, request):
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

        return redirect(request.META.get("HTTP_REFERER", "/"))
