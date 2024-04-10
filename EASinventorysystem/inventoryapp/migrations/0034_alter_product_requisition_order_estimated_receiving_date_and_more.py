# Generated by Django 5.0.2 on 2024-04-10 13:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0033_alter_product_product_stock_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_requisition_order',
            name='Estimated_Receiving_Date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase_order',
            name='Requested_Date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
