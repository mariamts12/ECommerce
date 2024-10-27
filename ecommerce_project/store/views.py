from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Product, ProductTag, Category


class IndexView(View):
    def get(self, request):

        products = Product.objects.all()
        context = {
            "products": products
        }

        return render(request, "index.html", context)


class CategoryView(ListView):
    model = Product
    template_name = "shop.html"
    context_object_name = "page_obj"
    paginate_by = 9

    def get_queryset(self):
        slug = self.kwargs.get('slug')

        if slug:
            categories = Category.objects.get_subcategories(slug)
            queryset = Product.objects.get_category_products(categories)
            self.subcategories = Category.objects.get_child_categories(slug)
        else:
            queryset = Product.objects.all().prefetch_related('tag')
            self.subcategories = Category.objects.get_top_categories()

        filter_price = self.request.GET.get('filter_price')
        filter_tag = self.request.GET.get('filter_tag')
        filter_name = self.request.GET.get('filter_name')

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
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        context.update({
                "page_obj": page_obj,
                "current_category": self.kwargs.get('slug', ""),
                "subcategories": self.subcategories,
                "tags": ProductTag.objects.all(),
                "get_elided_page_range": context["paginator"].get_elided_page_range(
                    self.request.GET.get('page', 1)
                )
            })
        return context


class ProductView(DetailView):
    model = Product
    template_name = "shop-detail.html"
