import mainapp.views as mainapp
from django.urls import path


app_name = "mainapp"

urlpatterns = [
    path("", mainapp.products, name="index"),
    path("category_<int:category_id>", mainapp.products, name="category"),
    path("<int:product_id>", mainapp.product, name="product"),
]
