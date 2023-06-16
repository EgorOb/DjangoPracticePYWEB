import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from store.models import Product, Category

if __name__ == "__main__":
    category = Category.objects.get(name='Vegetables')
    obj = Product(name='Carrots', description='Морковь', price=120,
                  image='static/products/product-7.jpg',
                  category=category)
    obj.save()

    obj = Product.objects.create(name='Fruit Juice',
                                 description='Фруктовый сок',
                                 price=120,
                                 image='static/products/product-8.jpg',
                                 category=Category.objects.get(name='Juice'))

    # data = ({'name': 'Bell Pepper',
    #          'description': 'Bell Pepper',
    #          'price': 120.00,
    #          'category': 'Vegetables',
    #          'image': 'static/products/product-1.jpg'},
    #         {'name': 'Strawberry',
    #          'description': 'Strawberry',
    #          'price': 120.00,
    #          'category': "Fruits",
    #          'image': 'static/products/product-2.jpg'},
    #         {'name': 'Green Beans',
    #          'description': 'Green Beans',
    #          'price': 120.00,
    #          'category': 'Vegetables',
    #          'image': 'static/products/product-3.jpg'},
    #         {'name': 'Purple Cabbage',
    #          'description': 'Purple Cabbage',
    #          'price': 120.00,
    #          'category': 'Vegetables',
    #          'image': 'static/products/product-4.jpg'},
    #         {'name': 'Tomatoe',
    #          'description': 'Tomatoe',
    #          'price': 120.00,
    #          'category': 'Vegetables',
    #          'image': 'static/products/product-5.jpg'},
    #         {'name': 'Brocolli',
    #          'description': 'Brocolli',
    #          'price': 120.00,
    #          'category': 'Vegetables',
    #          'image': 'static/products/product-6.jpg'})

    data = ({'name': 'Onion',
             'price': 120.00,
             'description': "Лук",
             'image': 'static/products/product-9.jpg',
             'category': 'Vegetables'},
            {'name': 'Apple',
             'price': 120.00,
             'description': "Яблоко",
             'image': 'static/products/product-10.jpg',
             'category': 'Fruits'},
            {'name': 'Garlic',
             'price': 120.00,
             'description': "Чеснок",
             'image': 'static/products/product-11.jpg',
             'category': 'Vegetables'},
            )

    categ = {'Fruits': Category.objects.get(name='Fruits'),
             'Vegetables': Category.objects.get(name='Vegetables'),
             }

    objects_to_create = [Product(name=val['name'],
                                 description=val['description'],
                                 price=val['price'],
                                 image=val['image'],
                                 category=categ[val['category']]) for val in
                         data]

    Product.objects.bulk_create(objects_to_create)

    # Product.objects.create(name='Chilli',
    #                        description='Перец Чили',
    #                        price=120,
    #                        image='static/products/product-12.jpg',
    #                        category=Category.objects.get(name='Vegetables'))
