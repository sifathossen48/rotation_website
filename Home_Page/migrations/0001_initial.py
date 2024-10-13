# Generated by Django 4.2 on 2024-10-08 09:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('background', models.ImageField(upload_to='slider/')),
                ('button_Link', models.URLField()),
            ],
        ),
    ]
