from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from apps.views import HomeView, ProductGridView, ProductDetailTemplateView, RegirsterFormView

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('product/grid', ProductGridView.as_view(), name='product_grid'),
    path('product/details', ProductDetailTemplateView.as_view(), name='product_detail')
]

urlpatterns += [
    path('auth/login', LoginView.as_view(template_name='apps/authentication/login.html'), name='login'),
    path('auth/logout', LogoutView.as_view(template_name='apps/authentication/login.html'), name='logout'),
    path('auth/register', RegirsterFormView.as_view(), name='register'),
]
