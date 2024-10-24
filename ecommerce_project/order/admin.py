from django.contrib import admin

from .models import Cart, CartItem


@admin.register(Cart)
class UserCartAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_select_related = ("user",)


@admin.register(CartItem)
class UserCartAdmin(admin.ModelAdmin):
    pass
