from django.urls import path

from .views import *

urlpatterns = [
    path("", store_home_page, name="store_home_page"),
    path("product/<slug:slug>/", product, name="product_details"),
    path("category/<slug:slug>", category, name="category_listing"),
    path("category/search/", search, name="search_view"),
    path("category/filter/", filter_view, name="filter_view"),
    path("category/", category, name="all_categories"),
    path("contact/", contact, name="contact"),
]
