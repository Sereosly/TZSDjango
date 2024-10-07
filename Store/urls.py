from django.urls import path
from .views import (HomeView, ProductListView,CategoryProductsView, ProductDetailView, ProfileView, RegisterView ,CustomLogoutView,)
from .favorite import toggle_favorite
from django.core.cache import cache

def clear_cache(request):
    cache.clear()
    return HttpResponse("Cache is cleared")

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Главная страница
    path('products/', ProductListView, name='product_list'),  # Список товаров
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Страница товара
    path('accounts/profile/', ProfileView.as_view(), name='profile'),  # Профиль пользователя
    path('register/', RegisterView.as_view(), name='register'),  # Маршрут для регистрации
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'), # Маршрут для выхода
    path('category/<int:category_id>/', CategoryProductsView, name='category_products'),# Список товаров по категории
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),# Просмотр продукта деталенее
    path('toggle_favorite/<int:product_id>/', toggle_favorite, name='toggle_favorite'),# переключение избранного
]
