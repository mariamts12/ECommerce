from django.urls import path
from django.views.generic import TemplateView

from .views import AddCartItem, CartView, DeleteCartItem, UpdateCartItem

app_name = "order"

urlpatterns = [
    path("cart/add/", AddCartItem.as_view(), name="add_item_to_cart"),
    path("cart/delete/<int:pk>", DeleteCartItem.as_view(), name="delete_item"),
    path("cart/update/<int:pk>", UpdateCartItem.as_view(), name="update_item"),
    path("cart/", CartView.as_view(), name="cart"),
    path(
        "checkout/",
        TemplateView.as_view(template_name="checkout.html"),
        name="checkout",
    ),
]
