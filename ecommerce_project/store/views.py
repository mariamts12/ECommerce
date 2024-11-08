from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.translation import get_language
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Category, Product, ProductTag


class IndexView(View):
    def get(self, request):
        language = get_language()

        products_cache_key = f"products_{language}"
        products = cache.get(products_cache_key)
        if not products:
            products = Product.objects.all().prefetch_related("tag")
            cache.set(products_cache_key, products, 300)

        category_cache_key = f"categories_{language}"
        categories = cache.get(category_cache_key)
        if not categories:
            categories = (
                Category.objects.prefetch_related("product_set")
                .filter(parent=None)
                .prefetch_related("product_set__tag")
            )
            cache.set(category_cache_key, categories, 300)

        context = {"products": products, "categories": categories}

        return render(request, "index.html", context)


# can't cache the whole view, because in that case global_context processor won't be executed
# so, the number of cart items in navbar won't be accurate
# @method_decorator(cache_page(60 * 5), name='get')
class CategoryView(ListView):
    model = Product
    template_name = "shop.html"
    context_object_name = "page_obj"
    paginate_by = 9

    def get_queryset(self):
        slug = self.kwargs.get("slug")

        if slug:
            categories = Category.objects.get_subcategories(slug)
            queryset = Product.objects.get_category_products(categories)
            self.subcategories = Category.objects.get_child_categories(slug)
        else:
            queryset = Product.objects.all().prefetch_related("tag")
            self.subcategories = Category.objects.get_top_categories()

        filter_price = self.request.GET.get("filter_price")
        filter_tag = self.request.GET.get("filter_tag")
        filter_name = self.request.GET.get("filter_name")

        if filter_tag:
            queryset = queryset.filter(tag__name=filter_tag)
        if filter_price and int(filter_price) != 0:
            queryset = queryset.filter(price__lte=filter_price)
        if filter_name:
            queryset = queryset.filter(name__icontains=filter_name)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page_number = self.request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)

        context.update(
            {
                "page_obj": page_obj,
                "current_category": self.kwargs.get("slug", ""),
                "subcategories": self.subcategories,
                "tags": ProductTag.objects.all(),
                "get_elided_page_range": context["paginator"].get_elided_page_range(
                    self.request.GET.get("page", 1)
                ),
            }
        )
        return context


class ProductView(DetailView):
    model = Product
    template_name = "shop-detail.html"

    def get_queryset(self):
        queryset = Product.objects.prefetch_related("category", "tag")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object

        language = get_language()

        cache_key = f"{product.id}_{language}"
        related_products = cache.get(cache_key)
        if not related_products:
            related_products = (
                Product.objects.filter(category__in=product.category.all())
                .exclude(pk=product.pk)
                .prefetch_related("tag")
                .annotate()
                .distinct()
            )

            for p in related_products:
                p.first_tag = p.tag.all()[0] if p.tag.exists() else None

            cache.set(cache_key, related_products, 300)

        context.update(
            {
                "related_products": related_products,
            }
        )
        return context
