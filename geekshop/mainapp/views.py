from unicodedata import category
from django.shortcuts import render, get_list_or_404
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
    return render(
        request,
        "mainapp/index.html",
        context={
            "title": title,
            "main_menu": MAIN_MENU,
            "products": products,
        },
    )


def products(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    title = "Продукты"
    MENU_CATEGORY = ProductCategory.objects.all()
    if pk is None:
        products = Product.objects.all().order_by("price")
    else:
        products = get_list_or_404(Product, category=pk)

    return render(
        request,
        "mainapp/products.html",
        context={
            "title": title,
            "main_menu": MAIN_MENU,
            "products_menu": MENU_CATEGORY,
            "products": products,
            "basket": basket,
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
