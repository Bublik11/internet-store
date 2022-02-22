from django.shortcuts import render
from mainapp.services import service_products, service_menu


def index(request):
    title = "Главная"
    products = service_products.get_products()[:4]
    menu = service_menu.change_main_menu(request.user)

    context = {
        "title": title,
        "main_menu": menu,
        "is_active": "домой",
        "products": products,
    }

    return render(request, "mainapp/index.html", context=context)


def products(request, category_id=None):
    title = "Продукты"
    hot_product = service_products.get_random_hot_product()
    products_menu = service_products.get_menu_products()
    menu = service_menu.change_main_menu(request.user)
    products = service_products.get_products(category_id)[:6]

    context = {
        "title": title,
        "main_menu": menu,
        "is_active": "продукты",
        "products_menu": products_menu,
        "products": products,
        "hot_product": hot_product,
    }

    return render(request, "mainapp/products.html", context=context)


def product(request, product_id=None):
    title = "Страница продукта"
    product = service_products.get_products(product_id=product_id)
    products_menu = service_products.get_menu_products()
    menu = service_menu.change_main_menu(request.user)

    context = {
        "title": title,
        "is_active": "продукты",
        "main_menu": menu,
        "products_menu": products_menu,
        "product": product,
    }

    return render(request, "mainapp/product.html", context=context)


def contact(request):
    title = "Контакты"
    menu = service_menu.change_main_menu(request.user)

    context = {
        "title": title,
        "is_active": "контакты",
        "main_menu": menu,
    }

    return render(request, "mainapp/contact.html", context=context)
