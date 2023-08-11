from django.urls import path

from grocery_store.order.views import place_order, order_history, order_confirmation, order_list, update_order_status

urlpatterns = [
    path('place_order/', place_order, name='place_order'),
    path('order_history/', order_history, name='order_history'),
    path('all_orders/', order_list, name='all_orders'),
    path('update_order/<int:pk>/', update_order_status, name='update_order_status'),
    path('order_confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),
]
