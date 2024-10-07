from django.db import models
from django.contrib.auth.models import AbstractUser

# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name

# Модель пользователя с избранными товарами
class User(AbstractUser):
    favorites = models.ManyToManyField(Product, related_name='favorited_by', blank=True)
