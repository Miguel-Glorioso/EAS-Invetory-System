# Generated by Django 5.0.1 on 2024-02-08 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0016_remove_product_consignee_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Category',
        ),
    ]
