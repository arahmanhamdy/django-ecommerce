from django.contrib import admin
from .models import ProductCategory, Product, ProductImage


class ImageInline(admin.StackedInline):
    model = ProductImage
    min_num = 1
    max_num = 4


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
