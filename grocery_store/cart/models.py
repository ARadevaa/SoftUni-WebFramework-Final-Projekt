# from django.contrib.auth import get_user_model
# from django.db import models
#
# from grocery_store.product.models import Product
#
# UserModel = get_user_model()
#
#
# class Cart(models.Model):
#     user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#
#     def __str__(self):
#         return f"Cart - User: {self.user.username} - Product: {self.product.name} - Quantity: {self.quantity}"
#
#     @property
#     def total_price(self):
#         return self.product.price * self.quantity
#
#
# def get_default_user():
#     UserModel = get_user_model()
#     return UserModel.objects.first()
#
#
# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"Cart - User: {self.cart.user.username} - Product: {self.product.name} - Quantity: {self.quantity}"
#
#     @property
#     def total_price(self):
#         return self.product.price * self.quantity