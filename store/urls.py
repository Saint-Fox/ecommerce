from django.urls import path
from .views import store_view, cart_view, checkout_view

urlpatterns = [
    path('', store_view, name='store-view'),
    path('cart/', cart_view, name='cart-view'),
    path('checkout/', checkout_view, name='checkout-view'),

]