from copy import deepcopy
from authapp.models import ShopUser

MAIN_MENU = [
    {"url": "main", "name": "домой"},
    {"url": "products:index", "name": "продукты"},
    {"url": "contact", "name": "контакты"},
]


def change_main_menu(user: ShopUser) -> list[dict[str, str]]:
    """
    Change the menu (MAIN_MENU) for a specific user (user)
    """

    menu = deepcopy(MAIN_MENU)

    if user.is_authenticated:
        add_menu_list = [
            {"url": "basket:view", "name": "корзина"},
            {"url": "auth:edit", "name": user.first_name},
            {"url": "auth:logout", "name": "выйти"},
        ]
    else:
        add_menu_list = [
            {"url": "auth:login", "name": "войти"},
        ]

    if user.is_superuser:
        add_menu_list.append({"url": "admin:users", "name": "админка"})
    menu.extend(add_menu_list)
    return menu
