
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages

from .forms import ProfileCreationForm, ProfileChangeForm
from catalog.models import Favorite
from catalog.forms import NavSearchForm


def signup(request):
    navbar_form = NavSearchForm()
    signup_form = AuthenticationForm = ProfileCreationForm()
    if request.method == 'POST':
        signup_form = AuthenticationForm = ProfileCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    context = {'navbar_form': navbar_form, 'signup_form': signup_form}
    return render(request, 'accounts/registration/signup.html', context)


def log_in(request):
    navbar_form = NavSearchForm()
    auth_form = AuthenticationForm()
    if request.method == 'POST':
        auth_form = AuthenticationForm(data=request.POST)
        if auth_form.is_valid():
            user = authenticate(
                username=auth_form.cleaned_data['username'],
                password=auth_form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        auth_form = AuthenticationForm()
    context = {'navbar_form': navbar_form, 'auth_form': auth_form}
    return render(request, 'accounts/registration/login.html', context)


def log_out(request):
    user = request.user
    logout(request)
    return redirect(settings.LOGIN_REDIRECT_URL)


@login_required
def account(request):
    navbar_form = NavSearchForm()
    profile = request.user
    context = { 'navbar_form': navbar_form, 'profile': profile,}
    return render(request, 'accounts/account.html', context)


@login_required
def favorites_list(request):
    navbar_form = NavSearchForm()
    profile = request.user
    favorites = profile.favorite_set.all()
    context = {'navbar_form': navbar_form, 'profile': profile, 'favorites': favorites}
    return render(request, 'accounts/favorites_list.html', context)


@login_required
def favorite_detail(request, favorite_pk):
    navbar_form = NavSearchForm()
    favorite = Favorite.objects.get(id=favorite_pk)
    context = {'navbar_form': navbar_form, 'favorite': favorite}
    return render(request, 'accounts/favorite_detail.html', context)


@login_required
def delete_favorite(request, favorite_pk):
    favorite = Favorite.objects.get(id=favorite_pk)
    if request.method == 'POST':
        favorite.delete()
        messages.success(request, f""""{favorite.substitute.name}" a bien été supprimé""")
    return redirect('favorites')
