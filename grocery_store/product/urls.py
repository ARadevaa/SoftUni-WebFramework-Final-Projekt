from django.urls import path, include

from grocery_store.product.views import product_add, product_edit, product_delete, product_detail\
    ,add_products_to_promo, promo_products

urlpatterns = (
    path('add/', product_add, name="product add"),
    path('add-to-promo/', add_products_to_promo, name='add_products_to_promo'),
    path('promo-products/', promo_products, name='promo_products'),
    path('<slug:product_name>/', include([
        path('', product_detail, name="product detail"),
        path('edit/', product_edit, name="product edit"),
        path('delete/', product_delete, name="product delete"),
    ]))
)
