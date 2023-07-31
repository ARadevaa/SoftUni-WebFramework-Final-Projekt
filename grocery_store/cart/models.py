from django.contrib.auth import get_user_model
from django.db import models
from grocery_store.product.models import Product

UserModel = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.name} - {self.product.name} - {self.quantity}"

    @property
    def total_price(self):
        return self.product.price * self.quantity


