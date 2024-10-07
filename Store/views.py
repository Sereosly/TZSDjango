from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from .models import Product, Category
from .mixins import FavoriteMixin
from django.views import View
from .forms import CustomUserCreationForm


class HomeView(FavoriteMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_products'] = Product.objects.all().order_by('?')[:10]

        context['categories'] = Category.objects.all()

        return context

def ProductListView(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_list.html', context)

def CategoryProductsView(request, category_id):
    # Получаем категорию по ID или возвращаем 404, если не найдена
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'category_products.html', context)

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
        context['templatetags'] = user.favorites.all()
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


class CustomLogoutView(LogoutView):
    def get_next_page(self):
        # Получаем URL из параметра next
        next_page = self.request.GET.get('next')

        if next_page == 'profile/':
            return '/'

        return next_page or '/'