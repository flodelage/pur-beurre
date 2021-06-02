
from django.shortcuts import render
from django.http import HttpResponse

from .models import Product


def products_list(request):
    products = Product.objects.all()

    context = {'products' : products,}

    return render(request, 'catalog/products_list.html', context)


def product_detail(request, product_pk):
    product = Product.objects.get(pk=product_pk)

    context = {'product': product,}

    return render(request, 'catalog/product_detail.html', context)
