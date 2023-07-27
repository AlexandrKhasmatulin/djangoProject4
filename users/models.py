import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=100, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='фото профиля',  **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна',  **NULLABLE)
    verification_key = models.TextField(uuid.uuid4(), **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []