import random
from django.shortcuts import get_list_or_404, get_object_or_404
from mainapp.models import Product, ProductCategory


def get_random_hot_product() -> Product:
    return random.choice(Product.objects.filter(discount__gt=0))


def get_menu_products() -> list[ProductCategory]:
    return ProductCategory.objects.all()


def get_products(category_id: int|None = None, product_id: int|None = None) -> list[Product]:
    if category_id is not None:
        return get_list_or_404(Product, category=category_id)
    elif product_id is not None:
        return get_object_or_404(Product, pk=product_id)
    else:
        return Product.objects.all()

