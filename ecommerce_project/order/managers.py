from django.db import models
from django.db.models import F, Sum


class CartItemManager(models.Manager):

    def get_cart_items(self, user_id: int):
        return self.filter(cart__user=user_id).annotate(
            total=F("product__price") * F("quantity")
        )

    def delete(self, item_id: int):
        item = self.get(id=item_id)
        item.delete()


class CartManager(models.Manager):

    def get_quantity(self, user_id):
        res = self.filter(user=user_id).aggregate(quantity=Sum("items__quantity"))
        if res["quantity"] is None:
            return 0
        return res["quantity"]
