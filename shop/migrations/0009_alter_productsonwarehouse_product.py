# Generated by Django 5.1.3 on 2024-11-17 00:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_productsonwarehouse_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsonwarehouse',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_records', to='shop.product'),
        ),
    ]