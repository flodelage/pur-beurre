
from django.urls import path
from catalog import views


urlpatterns = [
    path('products/', views.products_list, name='products_list'),
    path('product/<int:product_pk>', views.product_detail, name='product_detail')
]
