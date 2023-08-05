from django.contrib import admin

from grocery_store.product.models import Product, Promo


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available_quantity', 'category']
    search_fields = ['name']


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ['product', 'discount_percentage', 'discounted_price']
