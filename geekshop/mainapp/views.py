import json
from django.shortcuts import render

# Create your views here.

MAIN_MENU_LINKS = [
    {'url': 'main', 'name': 'домой'},
    {'url': 'products', 'name': 'продукты'},
    {'url': 'contact', 'name': 'контакты'},
]



def index(request):
    return render(request, 'mainapp/index.html', context= {
        'title': "Главная",
        'main_menu_links': MAIN_MENU_LINKS,
    })


def products(request):
    PRODUCTS_MENU_LINKS = [
        {'url': 'products_all', 'name': 'все'},
        {'url': 'products_home', 'name': 'дом'},
        {'url': 'products_office', 'name': 'офис'},
        {'url': 'products_modern', 'name': 'модерн'},
        {'url': 'products_classic', 'name': 'классика'},
    ]

    with open('./products.json', encoding='utf-8') as file:
        products = json.load(file)

    return render(request, 'mainapp/products.html', context= {
        'title': "Продукты",
        'main_menu_links': MAIN_MENU_LINKS,
        "products_menu_links": PRODUCTS_MENU_LINKS,
        "products": products,
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context= {
        'title': "Контакты",
        'main_menu_links': MAIN_MENU_LINKS,
    })
