# Generated by Django 5.0.7 on 2024-08-02 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventories', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FoodItem',
            new_name='FoodItemInventory',
        ),
    ]
