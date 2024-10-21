# Generated by Django 4.2 on 2024-10-14 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0011_brand_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='products/')),
                ('share_Link', models.URLField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home_Page.brand')),
            ],
        ),
    ]