from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from mainapp.services import service_menu, service_products
from basketapp.services import service_baskets
from django.template.loader import render_to_string
from django.http import JsonResponse


@login_required
def basket(request):
    title = "Ваша корзина"
    menu = service_menu.change_main_menu(request.user)

    context = {
        "title": title,
        "basket_items": request.user.basket.all(),
        "main_menu": menu,
        "is_active": "корзина"
    }

    return render(request, "basketapp/basket.html", context=context)


@login_required
def basket_add(request, product_id):
    product = service_products.get_products(product_id=product_id)
    service_baskets.add_product_to_basket(request.user, product)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def basket_remove(request, basket_id):
    service_baskets.remove_basket(basket_id=basket_id)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def basket_edit(request, basket_id, quantity):
    changed_basket = service_baskets.get_baskets(basket_id=basket_id)
    service_baskets.change_basket_quantity(changed_basket, new_quantity=quantity)
    basket_items = service_baskets.get_baskets(user=request.user).order_by('add_datetime')

    content = {
        'basket_items': basket_items,
    }

    result = render_to_string('basketapp/includes/inc_basket_list.html', context=content)

    return JsonResponse({'result': result})
