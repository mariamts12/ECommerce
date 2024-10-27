from django.urls import path
from django.views.generic import TemplateView

from .views import *


urlpatterns = [
    path('cart/add/', AddCartItemView.as_view(), name='add_item_to_cart'),
    path("cart/", CartView.as_view(), name="cart"),
    path("checkout/", TemplateView.as_view(template_name="checkout.html"), name="checkout"),
]
