from django import template

register = template.Library()

@register.filter
def is_favorite(product, user):
    # Проверяем, авторизован ли пользователь
    if user.is_authenticated:
        return product in user.favorites.all()
    return False