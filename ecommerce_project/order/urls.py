from django.urls import path
from .views import *


urlpatterns = [
    path("cart/", order_cart, name="cart"),
    path("checkout/", order_checkout, name="checkout"),
]
