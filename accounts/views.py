
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import ProfileCreationForm
from accounts.models import Profile
from catalog.models import Favorite


def home(request):
    user = request.user
    context = {'user': user}
    return render(request, 'accounts/home.html', context)


class SignUpView(CreateView):
    form_class = ProfileCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/registration/signup.html'


def logout_request(request):
    logout(request)
    profile = request.user
    username = profile.username

    context = {'username': username,}
    return render(request, 'accounts/registration/logout.html', context)


@login_required
def account(request):
    profile = request.user

    context = {'profile': profile,}
    return render(request, 'accounts/account.html', context)


@login_required
def favorites(request):
    profile = request.user
    favorites = profile.favorite_set.all()

    context = {'profile': profile, 'favorites': favorites}
    return render(request, 'accounts/favorites.html', context)
