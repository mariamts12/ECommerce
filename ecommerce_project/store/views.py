from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Category, Product


def store_home_page(request):
    return render(request, "index.html")


def category_listing(request, slug: str):
    context = {}
    return render(request, "shop.html", context)


def product(request, slug: str):
    context = {}
    return render(request, "shop-detail.html", context)


def contact(request):
    return render(request, "contact.html")
