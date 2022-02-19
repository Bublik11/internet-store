import random
from unicodedata import category
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Product, ProductCategory
from basketapp.models import Basket


MAIN_MENU = [
    {"url": "main", "name": "домой"},
    {"url": "products:index", "name": "продукты"},
    {"url": "contact", "name": "контакты"},
]


def index(request):
    title = "Главная"
    products = Product.objects.all()[:4]
    return render(request, "mainapp/index.html",
        context={
            "title": title,
            "main_menu": MAIN_MENU,
            "products": products,
        }
    )


def products(request, category_id=None):
    title = "Продукты"
    hot_product = random.choice(Product.objects.filter(discount__gt=0))
    products_menu = ProductCategory.objects.all()

    if category_id is None:
        products = Product.objects.all().order_by("price")[:6]
    else:
        products = get_list_or_404(Product, category=category_id)

    return render(
        request,
        "mainapp/products.html",
        context={
            "title": title,
            "main_menu": MAIN_MENU,
            "products_menu": products_menu,
            "products": products,
            "hot_product": hot_product,
        },
    )


def product(request, product_id=None):
    product = get_object_or_404(Product, id=product_id)
    title = product.name
    products_menu = ProductCategory.objects.all()

    return render(
        request,
        "mainapp/product.html",
        context={
            "title": title,
            "main_menu": MAIN_MENU,
            "products_menu": products_menu,
            "product": product,
        },
    )


def contact(request):
    title = "Контакты"
    return render(
        request,
        "mainapp/contact.html",
        context={
            "title": title,
            "main_menu": MAIN_MENU,
        },
    )
