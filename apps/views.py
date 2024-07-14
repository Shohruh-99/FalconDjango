from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, FormView

from apps.forms import RegisterForm
from apps.models import Product


class HomeView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'apps/product/product-list.html'
    context_object_name = 'products'


class ProductGridView(ListView):
    model = Product
    template_name = 'apps/product/product-grid.html'
    context_object_name = 'products'


class ProductDetailTemplateView(TemplateView):
    template_name = 'apps/product/product-details.html'


class RegirsterFormView(FormView):
    form_class = RegisterForm
    template_name = 'apps/authentication/register.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return redirect('login')