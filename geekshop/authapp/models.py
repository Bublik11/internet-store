from django.db import models
from django.contrib.auth.models import AbstractUser
 

class ShopUser(AbstractUser):
    user_photo = models.ImageField(
        verbose_name="Фото пользователя", upload_to="user_photo", blank=True
    )
    age = models.PositiveBigIntegerField(verbose_name="Возраст")
