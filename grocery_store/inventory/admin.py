from django.contrib import admin

from grocery_store.inventory.models import Delivery, Report


# Register your models here.
@admin.register(Delivery)
class DeliveryAddAdmin(admin.ModelAdmin):
    pass


@admin.register(Report)
class DeliveryReport(admin.ModelAdmin):
    pass
