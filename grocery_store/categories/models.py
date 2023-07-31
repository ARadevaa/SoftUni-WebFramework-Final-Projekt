from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=50
    )
    description = models.TextField(
        max_length=300,
        validators=(
            MinLengthValidator(10),
        ),
        blank=True,
        null=True
    )
    category_image = models.URLField(
        default="null",
    )

    def __str__(self):
        return f"{self.pk} - {self.name}"
