# Generated by Django 4.2.3 on 2023-07-20 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.URLField(default='null'),
        ),
    ]