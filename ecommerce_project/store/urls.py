from django.urls import path
from .views import *


urlpatterns = [
    path("", IndexView.as_view(), name="store_home_page"),
    path("product/<slug:slug>/", ProductView.as_view(), name="product_details"),
    path("category/<slug:slug>", CategoryView.as_view(), name="category_listing"),
    path("category/", CategoryView.as_view(), name="all_categories"),
    path("contact/", ContactView.as_view(), name="contact"),
]
