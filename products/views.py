from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ A view to all products, including dorting and filtering """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to a single product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)