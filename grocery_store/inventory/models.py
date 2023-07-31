from django.db import models

from grocery_store.product.models import Product


# Create your models here.
class Delivery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    delivery_date = models.DateField()

    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.product.product_quantity} - {self.delivery_date}"


class Report(models.Model):
    delivery_date = models.DateField()
    delivery = models.ForeignKey('Delivery', on_delete=models.CASCADE, default=None)
    quantity_delivered = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.delivery.product} - {self.delivery_date}"
