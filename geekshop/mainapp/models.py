from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name="Название категории", max_length=64, unique=True
    )
    description = models.TextField(verbose_name="Описание", blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory, verbose_name="Название категории", on_delete=models.CASCADE
    )
    name = models.CharField(verbose_name="Название товара", max_length=128)
    image = models.ImageField(
        verbose_name="Изображение", upload_to="products_image", blank=True
    )
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.DecimalField(
        verbose_name="Цена", max_digits=9, decimal_places=2, default=0
    )
    discount = models.PositiveIntegerField(
        verbose_name="Скидка", default=0
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Количество на складе", default=0
    )

    @property
    def discount_price(self):
        return round(self.price * (100 - self.discount))/100

    def __str__(self) -> str:
        return self.name
