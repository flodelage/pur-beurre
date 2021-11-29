
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages

from .forms import ProfileCreationForm
from catalog.models import Favorite
from catalog.forms import NavSearchForm


def signup(request):
    """
    Allow a user to register an account
    """
    navbar_form = NavSearchForm()
    signup_form = ProfileCreationForm()
    if request.method == 'POST':
        signup_form = ProfileCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    context = {'navbar_form': navbar_form, 'signup_form': signup_form}
    return render(request, 'accounts/registration/signup.html', context)


def log_in(request):
    """
    Allow a user to log in
    """
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


@login_required
def log_out(request):
    """
    Allow a logged in user to log out
    """
    logout(request)
    return redirect(settings.LOGIN_REDIRECT_URL)


@login_required
def account(request):
    """
    Allow a logged in user to access to his profile details
    """
    navbar_form = NavSearchForm()
    profile = request.user
    context = {'navbar_form': navbar_form, 'profile': profile, }
    return render(request, 'accounts/account.html', context)


@login_required
def favorites_list(request):
    """
    Allow a logged in user to see his profile details
    """
    navbar_form = NavSearchForm()
    profile = request.user
    favorites = profile.favorite_set.all()
    context = {'navbar_form': navbar_form,
               'profile': profile,
               'favorites': favorites, }
    return render(request, 'accounts/favorites_list.html', context)


@login_required
def favorite_detail(request, favorite_pk):
    """
    Allow a logged in user to see a favorite details
    """
    navbar_form = NavSearchForm()
    favorite = get_object_or_404(Favorite, id=favorite_pk)
    context = {'navbar_form': navbar_form, 'favorite': favorite, }
    return render(request, 'accounts/favorite_detail.html', context)


@login_required
def delete_favorite(request, favorite_pk):
    """
    Allow a logged in user to delete one favorite
    """
    favorite = get_object_or_404(Favorite, id=favorite_pk)
    if request.method == 'POST':
        favorite.delete()
        messages.success(
            request, f""""{favorite.substitute.name}" a bien été supprimé"""
        )
    return redirect('favorites')
