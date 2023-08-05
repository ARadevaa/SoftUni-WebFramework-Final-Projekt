from django.urls import path

from grocery_store.order.views import place_order, order_history, order_confirmation, all_orders

urlpatterns = [
    path('place_order/', place_order, name='place_order'),
    path('order_history/', order_history, name='order_history'),
    path('all_orders/', all_orders, name='all_orders'),
    path('order_confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),
]
