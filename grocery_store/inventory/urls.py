from django.urls import path

from grocery_store.inventory.views import delivery_add, inventory_details, delivery_report

urlpatterns = (
    path('add/', delivery_add, name='delivery add'),
    path('details', inventory_details, name='inventory details'),
    path('reports/', delivery_report, name='delivery reports'),
)
