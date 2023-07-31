from django.contrib import admin

from grocery_store.product.models import Product, Promo


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    pass
