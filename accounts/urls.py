
from django.urls import path

from .views import SignUpView
from accounts import views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', views.logout_request, name='logout'),
    path('account/', views.account, name='account'),
    path('favorites/', views.favorites, name="favorites"),
]
