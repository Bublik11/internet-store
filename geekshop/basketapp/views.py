from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product
from basketapp.models import Basket
from mainapp.views import MAIN_MENU
from django.template.loader import render_to_string
from django.http import JsonResponse


@login_required
def basket(request):

    return render(
        request,
        "basketapp/basket.html",
        context={
            "title": "Ваша корзина:",
            "basket_items": Basket.objects.filter(user=request.user),
            "main_menu": MAIN_MENU,
        },
    )


@login_required
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


@login_required
def basket_remove(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    basket.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def basket_edit(request, pk, quantity):
    quantity = quantity
    new_basket_item = Basket.objects.get(pk=int(pk))

    if quantity > 0:
        new_basket_item.quantity = quantity
        new_basket_item.save()
    else:
        new_basket_item.delete()

    basket_items = Basket.objects.filter(user=request.user).\
        order_by('product__category')

    content = {
        'basket_items': basket_items,
    }

    result = render_to_string('basketapp/includes/inc_basket_list.html',
                              content)

    return JsonResponse({'result': result})
