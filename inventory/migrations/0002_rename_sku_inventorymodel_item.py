# Generated by Django 4.0.5 on 2023-07-07 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventorymodel',
            old_name='sku',
            new_name='item',
        ),
    ]
