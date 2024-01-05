from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель для пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name="почта")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
