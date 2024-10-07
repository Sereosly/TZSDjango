from django.urls import path
from .views import home, product_list, ProductDetailView, ProfileView, RegisterView

urlpatterns = [
    path('', home, name='home'),  # Главная страница
    path('products/', product_list, name='product_list'),  # Список товаров
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Страница товара
    path('accounts/profile/', ProfileView.as_view(), name='profile'),  # Профиль пользователя
    path('register/', RegisterView.as_view(), name='register'),  # Маршрут для регистрации
]
