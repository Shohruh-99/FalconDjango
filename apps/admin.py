from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline

from apps.models import Product, Category, Specification, ProductImage

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    exclude = 'slug',

class SpecificationAdmin(StackedInline):
    model = Specification


class ProductImageAdmin(StackedInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    inlines = SpecificationAdmin, ProductImageAdmin
    exclude = 'slug',
