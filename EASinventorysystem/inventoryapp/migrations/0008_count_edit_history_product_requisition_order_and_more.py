# Generated by Django 5.0.1 on 2024-02-05 11:12

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0007_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Count_Edit_History',
            fields=[
                ('Count_Edit_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Date_Updated', models.DateTimeField(auto_now_add=True)),
                ('Initial_Inventory_Count', models.PositiveIntegerField()),
                ('Updated_Inventory_Count', models.PositiveIntegerField()),
                ('Image_Report', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Text_Report', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1024)])),
            ],
        ),
        migrations.CreateModel(
            name='Product_Requisition_Order',
            fields=[
                ('Product_Requisition_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Creation_Date', models.DateTimeField(auto_now_add=True)),
                ('Estimated_Receiving_Date', models.DateField()),
                ('Received_Date', models.DateTimeField(blank=True, null=True)),
                ('PRO_Manufacturer', models.CharField(max_length=32)),
                ('Total_Cost', models.DecimalField(decimal_places=2, max_digits=9)),
                ('Notes', models.TextField(blank=True, null=True)),
                ('Progress', models.CharField(max_length=16)),
                ('PRO_Status', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Order',
            fields=[
                ('Purchase_Order_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Creation_Date', models.DateTimeField(auto_now_add=True)),
                ('Requested_Date', models.DateField()),
                ('Fulfilled_Date', models.DateTimeField(blank=True, null=True)),
                ('Total_Due', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(0)])),
                ('Notes', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1024)])),
                ('Progress', models.CharField(max_length=16)),
                ('PO_Status', models.CharField(max_length=16)),
                ('Shipping_Method', models.CharField(max_length=32)),
                ('Order_Method', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='Product_Low_Stock_Threshold',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='low_stock_threshold',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='Actual_Inventory_Count',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='Reserved_Inventory_Count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='To_Be_Received_Inventory_Count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='Partially_Fulfilled_History',
            fields=[
                ('Partially_Fulfill_Edit_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Date_Updated', models.DateTimeField(auto_now_add=True)),
                ('Partially_Fulfilled_Quantity', models.PositiveIntegerField()),
                ('Image_Report', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Text_Report', models.TextField(blank=True, null=True)),
                ('Account_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.account')),
                ('Product_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.product')),
                ('Product_Requisition_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.product_requisition_order')),
            ],
        ),
    ]
