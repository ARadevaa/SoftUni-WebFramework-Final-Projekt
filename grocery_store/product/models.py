from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from grocery_store.categories.models import Category

UserModel = get_user_model()


class Product(models.Model):
    name = models.CharField(
        max_length=50
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    product_image = models.URLField()

    product_quantity = models.IntegerField()

    available_quantity = models.IntegerField(default=0)

    description = models.TextField(
        max_length=300,
        validators=(
            MinLengthValidator(10),
        ),
        blank=True,
        null=True
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True)

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        # call parent save
        # this way, we will have an instance
        # CREATE
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
        # UPDATE
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk} - {self.name} - {self.price} - {self.available_quantity} - {self.category}"


class Promo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    @property
    def calculate_discounted_price(self):
        if self.discount_percentage and self.product:
            discount = self.discount_percentage / 100
            self.discounted_price = self.product.price * (1 - discount)
            return self.discounted_price
        return None
