from django.urls import path, include

from grocery_store.product.views import product_add,  \
    add_products_to_promo, promo_products, ProductListView, ProductDetailView, ProductEditView, ProductDeleteView

urlpatterns = (
    path('add/', product_add, name="product add"),
    path('add-to-promo/', add_products_to_promo, name='add_products_to_promo'),
    path('promo-products/', promo_products, name='promo_products'),
    path('all-products/', ProductListView.as_view(), name="product list"),
    path('<slug:product_name>/', include([
        path('', ProductDetailView.as_view(), name='product detail'),
        path('edit/', ProductEditView.as_view(), name='product edit'),
        path('delete/', ProductDeleteView.as_view(), name="product delete"),
    ]))
)
