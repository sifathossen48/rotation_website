# Generated by Django 4.2 on 2024-05-25 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News_Page', '0003_newsgallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsgallery',
            name='photoName',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
