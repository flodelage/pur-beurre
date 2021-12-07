
from .forms import NavSearchForm


def nav_bar_form(request):
    navbar_form = NavSearchForm()
    return {'navbar_form': navbar_form}
