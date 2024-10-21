from django.shortcuts import render


def order_cart(request):
    return render(request, "cart.html")


def order_checkout(request):
    return render(request, "checkout.html")
