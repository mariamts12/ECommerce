from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from order.models import Cart

from .models import Product, ProductTag, Category


class IndexView(View):
    def get(self, request):
        cart_items_quantity = 0
        if request.user.is_authenticated:
            cart_items_quantity = Cart.objects.get_quantity(request.user.id)

        request.session["cart_items_quantity"] = cart_items_quantity
        products = Product.objects.all()
        context = {
            "products": products
        }

        return render(request, "index.html", context)


# pagination ain't working right
# class CategoryView(ListView):
#     model = Product
#     template_name = "shop.html"
#     context_object_name = "page_obj"
#     paginate_by = 9
#
#     def get_queryset(self):
#         slug = self.kwargs.get('slug', "")
#         queryset = super().get_queryset()
#
#         if slug:
#             categories = Category.objects.get_subcategories(slug)
#             queryset = queryset.filter(category__in=categories)
#             self.subcategories = Category.objects.get_child_categories(slug)
#         else:
#             self.subcategories = Category.objects.get_top_categories()
#
#         filter_price = self.request.GET.get('filter_price')
#         filter_tag = self.request.GET.get('filter_tag')
#         filter_name = self.request.GET.get('filter_name')
#
#         if filter_tag:
#             queryset = queryset.filter(tag__name=filter_tag)
#         if filter_price and int(filter_price) != 0:
#             queryset = queryset.filter(price__lte=filter_price)
#         if filter_name:
#             queryset = queryset.filter(name__icontains=filter_name)
#
#         return queryset.distinct()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context.update({
#                 "current_category": self.kwargs.get('slug', ""),
#                 "subcategories": self.subcategories,
#                 "tags": ProductTag.objects.all(),
#                 "get_elided_page_range": context["paginator"].get_elided_page_range(
#                     self.request.GET.get('page', 1)
#                 )
#             })
#         return context


# pagination works
class CategoryView2(View):
    def get(self, request, slug: str = ""):
        if slug == "":
            products = Product.objects.all()
            subcategories = Category.objects.get_top_categories()
        else:
            categories = Category.objects.get_subcategories(slug)
            products = Product.objects.get_category_products(categories)
            subcategories = Category.objects.get_child_categories(slug)

        filter_price = request.GET.get('filter_price')
        filter_tag = request.GET.get('filter_tag')
        filter_name = request.GET.get('filter_name')

        if filter_tag:
            products = products.filter(tag__name=filter_tag)
        if filter_price and int(filter_price) != 0:
            products = products.filter(price__lte=filter_price)
        if filter_name:
            products = products.filter(name__contains=filter_name)

        paginator = Paginator(products, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        tags = ProductTag.objects.all()
        if not page_number:
            page_number = 1

        context = {
            "page_obj": page_obj,
            "tags": tags,
            "subcategories": subcategories,
            "get_elided_page_range": paginator.get_elided_page_range(page_number),
            "current_category": slug,
        }
        return render(request, "shop.html", context)


class ProductView(DetailView):
    model = Product
    template_name = "shop-detail.html"


class ContactView(View):
    def get(self, request):
        return render(request, "contact.html")
