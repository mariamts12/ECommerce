from django.shortcuts import render, redirect
from django.views import View

from store.models import Product
from .models import Cart, CartItem


class CartView(View):
    def post(self, request):
        if 'delete_item_id' in request.POST:
            CartItem.objects.delete(request.POST.get('delete_item_id'))
        return self.get(request)

    def get(self, request):
        # if request.user.is_authenticated:
        user_id = request.user.id
        items = CartItem.objects.get_cart_items(user_id).prefetch_related('product')

        context = {
            "items": items
        }

        return render(request, "cart.html", context)


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

        return redirect(request.META.get('HTTP_REFERER', '/'))
