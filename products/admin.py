from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating'
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)