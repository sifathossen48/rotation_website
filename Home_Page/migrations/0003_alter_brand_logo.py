# Generated by Django 4.2 on 2024-10-08 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0002_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.FileField(upload_to='brand/'),
        ),
    ]
