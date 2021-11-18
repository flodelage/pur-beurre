
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Product, Category, Favorite
from .forms import SearchForm, HomeSearchForm, NavSearchForm


def home(request):
    home_form = HomeSearchForm()
    navbar_form = NavSearchForm()
    context = {'navbar_form': navbar_form, 'home_form': home_form,}
    return render(request, 'catalog/home.html', context)


def products_list(request):
    navbar_form = SearchForm()
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
        products = set(products)
        context = {'navbar_form': navbar_form, 'user_input': user_input, 'products': products,}
    else:
        navbar_form = NavSearchForm()
        context = {'navbar_form': navbar_form,}
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


@login_required
def favorite_save(request, product_pk, substitute_pk):
    if request.method != 'POST':
        return HttpResponseRedirect(request.path)

    product = Product.objects.get(pk=product_pk)
    substitute = Product.objects.get(pk=substitute_pk)
    profile = request.user
    favorite = Favorite(product=product, substitute=substitute, profile=profile)
    try:
        favorite.save()
        messages.success(
            request, f""""{favorite.substitute.name}" a bien été enregistré"""
        )
    except:
        messages.error(
            request,
            'Ce produit et ce substitut font déjà partie de vos favoris'
        )

    return redirect(reverse('substitutes_list', kwargs={'product_pk': product.id}))


def legal_mentions(request):
    navbar_form = NavSearchForm()
    return render(request, 'catalog/legal_mentions.html', context={'navbar_form': navbar_form,})
