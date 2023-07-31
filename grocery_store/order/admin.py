from django.contrib import admin

from grocery_store.order.models import Order


# Register your models here.
@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    pass
