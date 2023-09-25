from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from django.db.models import Q
from django.contrib import messages


def all_products(request):
    """ A view to all products, including dorting and filtering """

    products = Product.objects.all()
    query = None
    category = None
    sortkey = None

    if request.GET:

        if 'sort_by' in request.GET:
            sortkey = request.GET('sort_by')
            if sortkey == 'alpha_ascend':
                products = Product.objects.all.order_by('name').values()

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter the item you are looking for")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search': query,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to a single product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
