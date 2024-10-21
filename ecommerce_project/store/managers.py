from django.db import models
from django.db.models import F
from django.db.models.functions import Round


class CategoryManager(models.Manager):
    def get_subcategories(self, category_id: int) -> list[int]:
        categories = self.select_related('parent').all()
        return self.__get_subcategories_rec(categories, category_id)

    def __get_subcategories_rec(self, categories, category_id):
        sub = []
        for c in categories:
            if c.parent and c.parent.id == category_id:
                sub.append(c.id)
                sub += self.__get_subcategories_rec(categories, c.id)
        return sub

    def get_all(self) -> list:
        categories = self.all()
        result = []

        for c in categories:
            p = c.parent
            parent = None
            if p is not None:
                parent = {
                    "id": p.id,
                    "name": p.name,
                    "description": p.description
                }

            category = {
                "id": c.id,
                "name": c.name,
                "description": c.description,
                "parent": parent
            }
            result.append(category)
        return result


class ProductManager(models.Manager):
    def get_category_products(self, categories):
        products = (self.prefetch_related('category').filter(category__id__in=categories)
                    .annotate(total=Round(F("quantity")*F("price"), precision=2)))
        return products

    @staticmethod
    def most_expensive_product(products):
        return products.order_by("-price").first()

    @staticmethod
    def cheapest_product(products):
        return products.order_by("price").first()

    @staticmethod
    def average_price(products):
        avg = products.aggregate(avg=Avg('price'))['avg']
        return round(avg, 2)

    @staticmethod
    def get_total(products):
        total = products.aggregate(total_category_price=Sum('total'))['total_category_price']
        return round(total, 2)

    def get_all(self) -> list:
        products = self.prefetch_related('category')
        result = []

        for p in products:
            category_list = []
            for c in p.category.all():
                category = {
                    "id": c.id,
                    "name": c.name,
                    "description": c.description
                }
                category_list.append(category)

            image = str(p.image)
            if len(image) == 0:
                image = None
            product = {
                "id": p.id,
                "name": p.name,
                "description": p.description,
                "price": p.price,
                "image": image,
                "categories": category_list
            }
            result.append(product)
        return result
