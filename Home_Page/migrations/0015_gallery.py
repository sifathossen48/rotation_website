# Generated by Django 4.2 on 2024-10-14 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0014_remove_product_shop_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='brand/galleries/')),
                ('caption', models.CharField(blank=True, max_length=255, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='Home_Page.brand')),
            ],
        ),
    ]
