from django.urls import path

from grocery_store.order.views import place_order, order_history, order_confirmation

urlpatterns = [
    path('place_order/', place_order, name='place_order'),
    path('order_history/', order_history, name='order_history'),
    path('order_confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),
]
