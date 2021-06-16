
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import ProfileCreationForm
from accounts.models import Profile
from catalog.models import Favorite


class SignUpView(CreateView):
    form_class = ProfileCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/registration/signup.html'


def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


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


def favorite_save(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        substitute = request.POST.get('substitute')
        profile = request.POST.get('profile')
        Favorite.objects.create(
            product=product,
            substitute=substitute,
            profile=profile
        )
    return JsonResponse({"status": 'Success'})
