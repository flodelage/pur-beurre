
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q

from .models import Product, Category
from .forms import SearchForm, HomeSearchForm, NavSearchForm


def home(request):
    home_form = HomeSearchForm()
    navbar_form = NavSearchForm()
    context = {'navbar_form': navbar_form, 'home_form': home_form,}
    return render(request, 'catalog/home.html', context)


def products_list(request):
    navbar_form = NavSearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['search']
            if user_input == '':
                products = Product.objects.all()
            else:
                products = Product.objects.filter(
                    Q(name__icontains=user_input) | Q(categories__name__icontains=user_input)
                )
    else:
        navbar_form = NavSearchForm()
    products = set(products)
    context = {'navbar_form': navbar_form, 'user_input': user_input, 'products' : products,}
    return render(request, 'catalog/products_list.html', context)


def product_detail(request, product_pk):
    navbar_form = NavSearchForm()
    product = Product.objects.get(pk=product_pk)
    context = {'product': product, 'navbar_form': navbar_form}
    return render(request, 'catalog/product_detail.html', context)


def substitutes_list(request, product_pk):
    navbar_form = NavSearchForm()
    product = Product.objects.get(pk=product_pk)
    categories = Category.objects.filter(products__id=product.id)
    substitutes = Product.objects.filter(categories__in=categories, nutriscore__lt=product.nutriscore)
    substitutes = set(substitutes)
    context = {'navbar_form': navbar_form ,'categories': categories, 'product': product, 'substitutes': substitutes,}
    return render(request, 'catalog/substitutes_list.html', context)


def substitute_detail(request, substitute_pk):
    product = Product.objects.get(pk=substitute_pk)
    context = {'product': product,}
    return render(request, 'catalog/product_detail.html', context)


def favorite_save(request):
    favorite = request.POST.get("favorite")
    return JsonResponse({"favorite": favorite})


def legal_mentions(request):
    navbar_form = NavSearchForm()
    return render(request, 'catalog/legal_mentions.html', context={'navbar_form': navbar_form,})
