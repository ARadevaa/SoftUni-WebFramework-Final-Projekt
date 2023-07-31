from django.db import models
from django.contrib.auth import get_user_model

from grocery_store.cart.models import Cart
from grocery_store.product.models import Product

UserModel = get_user_model()


class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    )
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.created_at}"


