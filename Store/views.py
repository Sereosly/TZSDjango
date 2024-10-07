from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Category
from .mixins import FavoriteMixin
from django.views import View
from .forms import CustomUserCreationForm


# Главная страница, которая показывает случайные товары (5-10)
def home(request):
    products = Product.objects.order_by('?')[:10]
    return render(request, 'home.html', {'products': products})


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    # Фильтрация по категории
    category = request.GET.get('category')
    if category:
        products = products.filter(category_id=category)

    # Фильтрация по диапазону цен
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    return render(request, 'product_list.html', {'products': products, 'categories': categories})


class ProductDetailView(FavoriteMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['is_favorite'] = self.is_favorite(product)
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['favorites'] = user.favorites.all()
        return context

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Замените на вашу страницу логина
        return render(request, 'registration/register.html', {'form': form})