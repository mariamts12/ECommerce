from django.urls import path
from .views import *


urlpatterns = [
    path('cart/add/', add_item_to_cart, name='add_item_to_cart'),
    path("cart/", cart, name="cart"),
    path("checkout/", order_checkout, name="checkout"),
]
