from django.core.management.base import BaseCommand
from order.models import CartItem
from django.db.models import Count


class Command(BaseCommand):
    help = 'Displays the top 3 most popular products'

    def handle(self, *args, **options):
        items = (
            CartItem.objects
            .values('product__name')
            .annotate(user_count=Count('cart__user', distinct=True))
            .order_by('-user_count')[:3]
        )

        self.stdout.write("The top 3 most popular products:")

        for item in items:
            self.stdout.write(
                f"{item['product__name']} - in the cart of {item['user_count']} users"
            )
