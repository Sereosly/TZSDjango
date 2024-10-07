from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.http import JsonResponse

@login_required
def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.favorites.filter(id=product.id).exists():
        request.user.favorites.remove(product)
    else:
        request.user.favorites.add(product)

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def user_profile(request):
    favorites = request.user.favorites.all()
    return render(request, 'user_profile.html', {'favorites': favorites})