from django.shortcuts import get_object_or_404
from authapp.models import ShopUser
from basketapp.models import Basket
from mainapp.models import Product


def add_product_to_basket(user: ShopUser, product: Product) -> None:
    """
    Adds a product to the user's cart
    """

    basket_items = Basket.objects.filter(user=user, product=product)

    if basket_items:
        basket = basket_items.first()
    else:
        basket = Basket(user=user, product=product)
    basket.quantity += 1
    basket.save()


def remove_basket(basket_id: int) -> None:
    """
    Remove basket with pk=basket_id
    """

    basket = get_object_or_404(Basket, pk=basket_id)
    basket.delete()


def get_baskets(basket_id: int | None = None, user: ShopUser | None = None) -> Basket | list[Basket]:
    if basket_id is not None:
        return get_object_or_404(Basket, pk=basket_id)
    elif user is not None:
        return user.basket.all()
    else:
        return Basket.objects.all()


def change_basket_quantity(basket: Basket, new_quantity: int | None = None, delta_quantity: int | None = 0) -> None:
    if new_quantity is not None:
        basket.quantity = new_quantity
        basket.save()
        return
    elif delta_quantity != 0:
        basket.quantity += delta_quantity
        basket.save()
        return

