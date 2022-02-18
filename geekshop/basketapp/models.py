from enum import unique
from locale import format_string
from pickle import TRUE
from django.conf import settings
from django.db import models
from mainapp.models import Product


class BasketManager(models.Manager):
    def count(self):
        return len(self.all())

    def sum(self):
        sum = 0
        basket = self.all()
        for item in basket:
            sum += item.product.price * item.quantity
        return sum


class Basket(models.Model):
    class Meta:
        unique_together = ["user", "product"]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="basket"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="количество", default=0)
    add_datetime = models.DateTimeField(
        verbose_name="время добавления", auto_now_add=True
    )

    objects = BasketManager()

    def __str__(self) -> str:
        return f"{self.product.name} - {self.quantity} шт."
