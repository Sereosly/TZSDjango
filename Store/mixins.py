class FavoriteMixin:
    def is_favorite(self, product):
        user = self.request.user
        if user.is_authenticated:
            return user.favorites.filter(id=product.id).exists()
        return False
