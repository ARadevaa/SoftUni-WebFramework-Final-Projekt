
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('grocery_store.common.urls')),
    path('address/', include('grocery_store.address.urls')),
    path('cart/', include('grocery_store.cart.urls')),
    path('categories/', include('grocery_store.categories.urls')),
    path('order/', include('grocery_store.order.urls')),
    path('payment/', include('grocery_store.payment.urls')),
    path('product/', include('grocery_store.product.urls')),
    path('user_profile/', include('grocery_store.user_profile.urls')),
    path('inventory/', include('grocery_store.inventory.urls')),
]
