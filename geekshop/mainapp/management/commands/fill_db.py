import json, os

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product
from django.core.management.base import BaseCommand

JSON_PUTH = "mainapp/json"


def load_from_json(file_name):
    with open(
        os.path.join(JSON_PUTH, file_name + ".json"), "r", encoding="utf-8"
    ) as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json("categories")

        ProductCategory.objects.all().delete
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json("products")
        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            category = ProductCategory.objects.get(name=category_name)
            product["category"] = category
            new_product = Product(**product)
            new_product.save()

        # For example
        ShopUser.objects.create_superuser("admin", "admin@admin", "adminadmin", age=25)
