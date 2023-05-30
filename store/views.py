from django.shortcuts import render
from django.views import View


class ShopView(View):

    def get(self, request):
        context = {'data': [{'name': 'Bell Pepper',
                             'discount': 30,
                             'price_before': 120.00,
                             'price_after': 80.00,
                             'url': 'store/images/product-1.jpg'},
                            {'name': 'Strawberry',
                             'discount': None,
                             'price_before': 120.00,
                             'url': 'store/images/product-2.jpg'},
                            {'name': 'Green Beans',
                             'discount': None,
                             'price_before': 120.00,
                             'url': 'store/images/product-3.jpg'},
                            {'name': 'Purple Cabbage',
                             'discount': None,
                             'price_before': 120.00,
                             'url': 'store/images/product-4.jpg'},
                            {'name': 'Tomatoe',
                             'discount': 30,
                             'price_before': 120.00,
                             'price_after': 80.00,
                             'url': 'store/images/product-5.jpg'},
                            {'name': 'Brocolli',
                             'discount': None,
                             'price_before': 120.00,
                             'url': 'store/images/product-6.jpg'},
                            {'name': 'Carrots',
                             'discount': None,
                             'price_before': 120.00,
                             'url': 'store/images/product-7.jpg'},
                            {'name': 'Fruit Juice',
                             'discount': None,
                             'price_before': 120.00,
                             'url': 'store/images/product-8.jpg'},
                            {'name': 'Onion',
                             'discount': 30,
                             'price_before': 120.00,
                             'price_after': 80.00,
                             'url': 'store/images/product-9.jpg'},
                            {'name': 'Apple',
                             'discount': None,
                             'price_before': 120.00,
                             'url': 'store/images/product-10.jpg'},
                            {'name': 'Garlic',
                             'discount': None,
                             'price_before': 120.00,
                             'url': 'store/images/product-11.jpg'},
                            {'name': 'Chilli',
                             'discount': None,
                             'price_before': 120.00,
                             'url': 'store/images/product-12.jpg'},
                            ]
                   }

        return render(request, 'store/shop.html', context)


class CartView(View):

    def get(self, request):
        return render(request, "store/cart.html")


class ProductSingleView(View):

    def get(self, request):
        return render(request, "store/product-single.html")
