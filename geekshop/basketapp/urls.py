from django.urls import path

import basketapp.views as basket

app_name = "basketapp"

urlpatterns = [
    path("", basket.basket, name="view"),
    path("add/<int:product_id>/", basket.basket_add, name="add"),
    path("remove/<int:basket_id>/", basket.basket_remove, name="remove"),
    path('edit/<int:basket_id>/<int:quantity>/', basket.basket_edit, name='edit'),
]
