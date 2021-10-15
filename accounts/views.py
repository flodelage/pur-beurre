
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings

from .forms import ProfileCreationForm, ProfileChangeForm
from accounts.models import Profile
from catalog.models import Favorite


def signup(request):
    form = ProfileCreationForm()
    if request.method == 'POST':
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'accounts/registration/signup.html', context={'form': form})


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/registration/login.html', context={'form': form})


def log_out(request):
    logout(request)
    return redirect(settings.LOGIN_REDIRECT_URL)


@login_required
def account(request):
    profile = request.user

    context = {'profile': profile,}
    return render(request, 'accounts/account.html', context)


@login_required
def favorites_list(request):
    profile = request.user
    favorites = profile.favorite_set.all()

    context = {'profile': profile, 'favorites': favorites}
    return render(request, 'accounts/favorites_list.html', context)
