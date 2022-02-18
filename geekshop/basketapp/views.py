from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product
from basketapp.models import Basket
from mainapp.views import MAIN_MENU


def basket(request):

    return render(
        request,
        "basketapp/basket.html",
        context={
            "title": "Ваша корзина:",
            "basket": Basket.objects.filter(user=request.user),
            "main_menu": MAIN_MENU,
        },
    )


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    basket_items = Basket.objects.filter(user=request.user, product=product)

    if basket_items:
        basket = basket_items.first()
    else:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1

    basket.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def basket_remove(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    basket.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
