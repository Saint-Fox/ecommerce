from django.urls import path
from .views import store_view, cart_view, checkout_view, update_item_view, process_order

urlpatterns = [
    path('', store_view, name='store-view'),
    path('cart/', cart_view, name='cart-view'),
    path('checkout/', checkout_view, name='checkout-view'),

    path('update_item/', update_item_view, name='update-item-view'),
    path('process_order/', process_order, name='process_order')
]