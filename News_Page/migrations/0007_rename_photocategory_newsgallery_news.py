# Generated by Django 4.2 on 2024-05-25 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News_Page', '0006_alter_news_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsgallery',
            old_name='photoCategory',
            new_name='news',
        ),
    ]