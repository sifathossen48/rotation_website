# Generated by Django 4.2 on 2024-10-14 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0012_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='share_Link',
            new_name='shop_Link',
        ),
    ]
