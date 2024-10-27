from django.db import models
from django.db.models import F
from django.db.models.functions import Round


class CategoryManager(models.Manager):

    def get_top_categories(self):
        return self.filter(parent=None)

    def get_child_categories(self, category_slug: str):
        return self.filter(parent__slug=category_slug)

    def get_subcategories(self, category_slug: str) -> list[int]:
        categories = self.select_related('parent').all()
        return self.__get_subcategories_rec(categories, category_slug)

    def __get_subcategories_rec(self, categories, category_slug):
        sub = []
        for c in categories:
            if c.parent and c.parent.slug == category_slug:
                sub.append(c.id)
                sub += self.__get_subcategories_rec(categories, c.id)
            else:
                if c.slug == category_slug:
                    sub.append(c.id)
        return sub


class ProductTagManager(models.Manager):
    pass


class ProductManager(models.Manager):
    def get_category_products(self, categories):
        products = (self.prefetch_related('tag').filter(category__id__in=categories)
                    .annotate(total=Round(F("quantity")*F("price"), precision=2)).distinct())
        return products

    def get_all(self) -> list:
        return self.prefetch_related('tag')
