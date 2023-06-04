from django.shortcuts import render
from django.views import View
from django.db.models import OuterRef, Subquery, F, ExpressionWrapper, DecimalField
from .models import Product, Discount


class ShopView(View):

    def get(self, request):
        price_with_discount = ExpressionWrapper(
            F('price') * (100.0 - F('discount_value')) / 100.0,
            output_field=DecimalField(max_digits=10, decimal_places=2)
        )

        products = Product.objects.annotate(
            discount_value=Subquery(
                Discount.objects.filter(product_id=OuterRef('id')).values(
                    'value')
            ),
            price_before=F('price'),
            price_after=price_with_discount
        ).values('id', 'name', 'image', 'price_before', 'price_after',
                 'discount_value')
        return render(request, 'store/shop.html', {"data": products})


class CartView(View):

    def get(self, request):
        return render(request, "store/cart.html")


class ProductSingleView(View):

    def get(self, request, id):
        data = {1: {'name': 'Bell Pepper',
                    'description': 'Bell Pepper',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-1.jpg'},
                2: {'name': 'Strawberry',
                    'description': 'Strawberry',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-2.jpg'},
                3: {'name': 'Green Beans',
                    'description': 'Green Beans',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-3.jpg'},
                4: {'name': 'Purple Cabbage',
                    'description': 'Purple Cabbage',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-4.jpg'},
                5: {'name': 'Tomatoe',
                    'description': 'Tomatoe',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-5.jpg'},
                6: {'name': 'Brocolli',
                    'description': 'Brocolli',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-6.jpg'},
                7: {'name': 'Carrots',
                    'description': 'Carrots',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-7.jpg'},
                8: {'name': 'Fruit Juice',
                    'description': 'Fruit Juice',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-8.jpg'},
                9: {'name': 'Onion',
                    'description': 'Onion',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-9.jpg'},
                10: {'name': 'Apple',
                     'description': 'Apple',
                     'price': 120.00,
                     'rating': 5.0,
                     'url': 'store/images/product-10.jpg'},
                11: {'name': 'Garlic',
                     'description': 'Garlic',
                     'price': 120.00,
                     'rating': 5.0,
                     'url': 'store/images/product-11.jpg'},
                12: {'name': 'Chilli',
                     'description': 'Chilli',
                     'price': 120.00,
                     'rating': 5.0,
                     'url': 'store/images/product-12.jpg'}
                }
        return render(request, "store/product-single.html", context=data[id])
