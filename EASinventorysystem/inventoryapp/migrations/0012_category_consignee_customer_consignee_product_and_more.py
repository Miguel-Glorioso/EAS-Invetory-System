# Generated by Django 5.0.1 on 2024-02-07 08:15

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0011_delete_category_delete_count_edit_history_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Category_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Category_Name', models.CharField(max_length=32)),
                ('Category_Hex_Color_ID', models.CharField(max_length=7)),
                ('Description', models.TextField(validators=[django.core.validators.MaxLengthValidator(1024)])),
                ('Category_Product_Low_Stock_Threshold', models.PositiveIntegerField(validators=[django.core.validators.MaxLengthValidator(4)])),
                ('Notes', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1024)])),
            ],
        ),
        migrations.CreateModel(
            name='Consignee',
            fields=[
                ('Consignee_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Consignee_Tag_ID', models.CharField(max_length=32)),
                ('Customer_Name', models.CharField(max_length=32)),
                ('Address_Line_1', models.CharField(max_length=128)),
                ('Barangay', models.CharField(max_length=64)),
                ('Municipality', models.CharField(max_length=64)),
                ('Province', models.CharField(max_length=64)),
                ('Zip_Code', models.PositiveIntegerField(validators=[django.core.validators.MaxLengthValidator(4)])),
                ('Primary_Contact_Number', models.CharField(max_length=11)),
                ('Customer_Type', models.CharField(max_length=16)),
                ('Notes', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1024)])),
                ('Consignment_Period_Start', models.DateField()),
                ('Consignment_Period_End', models.DateField()),
                ('Emergency_Contact_Number', models.CharField(max_length=11)),
                ('Email_Address', models.EmailField(max_length=128)),
                ('Tag_Hex_Color_ID', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Customer_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Customer_Name', models.CharField(max_length=32)),
                ('Address_Line_1', models.CharField(max_length=128)),
                ('Barangay', models.CharField(max_length=64)),
                ('Municipality', models.CharField(max_length=64)),
                ('Province', models.CharField(max_length=64)),
                ('Zip_Code', models.PositiveIntegerField(validators=[django.core.validators.MaxLengthValidator(4)])),
                ('Primary_Contact_Number', models.CharField(max_length=11)),
                ('Customer_Type', models.CharField(max_length=16)),
                ('Notes', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1024)])),
            ],
        ),
        migrations.CreateModel(
            name='Consignee_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Consignee_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.consignee')),
                ('Product_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Count_Edit_History',
            fields=[
                ('Count_Edit_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Date_Updated', models.DateTimeField(auto_now_add=True)),
                ('Initial_Inventory_Count', models.PositiveIntegerField(validators=[django.core.validators.MaxLengthValidator(4)])),
                ('Updated_Inventory_Count', models.PositiveIntegerField(validators=[django.core.validators.MaxLengthValidator(4)])),
                ('Image_Report', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Text_Report', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1024)])),
                ('Account_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.account')),
                ('Product_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Requisition_Order',
            fields=[
                ('Product_Requisition_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Creation_Date', models.DateTimeField(auto_now_add=True)),
                ('Estimated_Receiving_Date', models.DateField(blank=True, null=True)),
                ('Received_Date', models.DateTimeField(blank=True, null=True)),
                ('PRO_Manufacturer', models.CharField(max_length=32)),
                ('Total_Cost', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(0)])),
                ('Notes', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1024)])),
                ('Progress', models.CharField(default='Pending', max_length=16)),
                ('PRO_Status', models.CharField(default='Ongoing', max_length=16)),
                ('Account_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.account')),
            ],
        ),
        migrations.CreateModel(
            name='Partially_Fulfilled_History',
            fields=[
                ('Partially_Fulfill_Edit_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Date_Updated', models.DateTimeField(auto_now_add=True)),
                ('Partially_Fulfilled_Quantity', models.PositiveIntegerField(validators=[django.core.validators.MaxLengthValidator(4)])),
                ('Image_Report', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Text_Report', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1024)])),
                ('Account_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.account')),
                ('Product_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.product')),
                ('Product_Requisition_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.product_requisition_order')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Order',
            fields=[
                ('Purchase_Order_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Creation_Date', models.DateTimeField(auto_now_add=True)),
                ('Requested_Date', models.DateField(blank=True, null=True)),
                ('Fulfilled_Date', models.DateTimeField(blank=True, null=True)),
                ('Total_Due', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(0)])),
                ('Notes', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1024)])),
                ('Progress', models.CharField(default='Pending', max_length=16)),
                ('PO_Status', models.CharField(default='Unfulfilled', max_length=16)),
                ('Shipping_Method', models.CharField(max_length=32)),
                ('Order_Method', models.CharField(max_length=32)),
                ('Account_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.account')),
                ('Consignee_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.consignee')),
                ('Customer_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Products_Ordered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveIntegerField(validators=[django.core.validators.MaxLengthValidator(4)])),
                ('Product_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.product')),
                ('Purchase_Order_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.purchase_order')),
            ],
        ),
        migrations.CreateModel(
            name='Stocks_Ordered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveIntegerField(validators=[django.core.validators.MaxLengthValidator(4)])),
                ('Product_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.product')),
                ('Product_Requisition_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.product_requisition_order')),
            ],
        ),
    ]
