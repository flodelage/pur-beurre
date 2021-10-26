
from django.urls import path

from accounts import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('account/', views.account, name='account'),
    path('favorites/', views.favorites_list, name='favorites'),
    path('delete_favorite/<int:favorite_pk>', views.delete_favorite, name='delete_favorite'),
]
