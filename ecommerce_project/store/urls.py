from django.urls import path
from django.views.generic import TemplateView

from .views import CategoryView, IndexView, ProductView

app_name = "store"

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("product/<slug:slug>/", ProductView.as_view(), name="product_details"),
    path("category/<slug:slug>", CategoryView.as_view(), name="category_listing"),
    path("category/", CategoryView.as_view(), name="all_categories"),
    path(
        "contact/", TemplateView.as_view(template_name="contact.html"), name="contact"
    ),
]
