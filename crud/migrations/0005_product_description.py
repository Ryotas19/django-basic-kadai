# Generated by Django 5.2.1 on 2025-05-31 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crud", "0004_remove_product_category_product_img_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
