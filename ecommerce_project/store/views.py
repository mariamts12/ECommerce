from django.core.paginator import Paginator
from django.shortcuts import render
from order.models import Cart

from .models import Product, ProductTag, Category


def store_home_page(request):
    cart_items_quantity = 0
    if request.user.is_authenticated:
        cart_items_quantity = Cart.objects.get_quantity(request.user.id)

    request.session["cart_items_quantity"] = cart_items_quantity
    products = Product.objects.get_all()
    context = {
        "products": products
    }

    return render(request, "index.html", context)


def category(request, slug: str = ""):
    if slug == "":
        products = Product.objects.get_all()
        subcategories = Category.objects.get_top_categories()
    else:
        categories = Category.objects.get_subcategories(slug)
        products = Product.objects.get_category_products(categories)
        subcategories = Category.objects.get_child_categories(slug)

    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tags = ProductTag.objects.all()

    context = {
        "page_obj": page_obj,
        "tags": tags,
        "subcategories": subcategories,
    }
    return render(request, "shop.html", context)


def product(request, slug: str):
    context = {}
    return render(request, "shop-detail.html", context)


def search(request):
    filter_name = request.GET.get('filter_name')

    if filter_name is not None:
        products = Product.objects.filter(name__contains=filter_name)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tags = ProductTag.objects.all()
    subcategories = Category.objects.get_top_categories()

    context = {
        "page_obj": page_obj,
        "tags": tags,
        "subcategories": subcategories,
    }

    return render(request, "shop.html", context)


def filter_view(request):
    filter_price = request.GET.get('filter_price')
    filter_tag = request.GET.get('filter_tag')
    tags = ProductTag.objects.all()
    subcategories = Category.objects.get_top_categories()
    print(filter_tag)
    print(filter_price)
    if int(filter_price) != 0 and filter_tag is not None:
        products = Product.objects.filter(price__lte=filter_price, tag__name=filter_tag)
    elif int(filter_price) != 0:
        products = Product.objects.filter(price__lte=filter_price)
    elif filter_tag is not None:
        products = Product.objects.filter(tag__name=filter_tag)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "tags": tags,
        "subcategories": subcategories,
    }

    return render(request, "shop.html", context)


def contact(request):
    return render(request, "contact.html")
