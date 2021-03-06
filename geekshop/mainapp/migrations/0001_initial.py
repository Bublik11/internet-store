# Generated by Django 4.0.2 on 2022-02-17 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=64, unique=True, verbose_name="Название категории"
                    ),
                ),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=128, verbose_name="Название товара"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        upload_to="products_image",
                        verbose_name="Изображение",
                    ),
                ),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=9, verbose_name="Цена"
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Количество на складе"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.productcategory",
                        verbose_name="Название категории",
                    ),
                ),
            ],
        ),
    ]
