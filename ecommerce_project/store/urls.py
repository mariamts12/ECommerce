from django.urls import path

from .views import *

urlpatterns = [
    path("", store_home_page, name="store_home_page"),
    path("product/<slug:slug>/", product, name="product_details"),
    path("category/<slug:slug>", category_listing, name="category_listing"),
    path("contact/", contact, name="contact"),
]
