# Generated by Django 5.0.2 on 2024-02-12 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_category_table_alter_product_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='Categories',
        ),
        migrations.AlterModelTable(
            name='product',
            table='Products',
        ),
    ]
