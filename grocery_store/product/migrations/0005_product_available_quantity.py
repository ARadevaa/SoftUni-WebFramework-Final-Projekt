# Generated by Django 4.2.3 on 2023-07-28 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_promo_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
