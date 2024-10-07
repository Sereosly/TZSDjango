from django.db import models
from django.contrib.auth.models import AbstractUser

# Модель для категории товаров
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Модель для товаров
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')  # Связь с категорией
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)  # Поле для изображений
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class User(AbstractUser):
    email = models.EmailField(unique=True)
    favorites = models.ManyToManyField('Product', related_name='favorited_by', blank=True)

    def __str__(self):
        return self.username