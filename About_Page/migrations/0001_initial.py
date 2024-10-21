# Generated by Django 4.2 on 2024-10-14 16:19

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_Title', models.CharField(max_length=30)),
                ('hero_Image', models.ImageField(upload_to='about/')),
                ('chairman_Image', models.ImageField(upload_to='about/')),
                ('chairman_Message', ckeditor.fields.RichTextField()),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
