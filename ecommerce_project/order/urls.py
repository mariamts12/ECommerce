from django.urls import path
from .views import *


urlpatterns = [
    path('cart/add/', AddCartItemView.as_view(), name='add_item_to_cart'),
    path("cart/", CartView.as_view(), name="cart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
]
