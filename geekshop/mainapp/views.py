from django.shortcuts import render
from .models import Product, ProductCategory


MAIN_MENU_LINKS = [
    {"url": "main", "name": "домой"},
    {"url": "products:index", "name": "продукты"},
    {"url": "contact", "name": "контакты"},
]


def index(request):
    title = "Главная"
    products = Product.objects.all()[:4]
    return render(
        request,
        "mainapp/index.html",
        context={
            "title": title,
            "main_menu_links": MAIN_MENU_LINKS,
            "products": products,
        },
    )


def products(request, pk=None):
    title = "Продукты"
    MENU_CATEGORY = ProductCategory.objects.all()
    if pk is None:
        products = Product.objects.all()[:3]
    else:
        products = Product.objects.filter(category=pk)[:3]

    return render(
        request,
        "mainapp/products.html",
        context={
            "title": title,
            "main_menu_links": MAIN_MENU_LINKS,
            "products_menu_links": MENU_CATEGORY,
            "products": products,
        },
    )


def contact(request):
    title = "Контакты"
    return render(
        request,
        "mainapp/contact.html",
        context={
            "title": title,
            "main_menu_links": MAIN_MENU_LINKS,
        },
    )
