# Generated by Django 5.0.2 on 2024-04-16 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0008_rename_article_articles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articles',
            new_name='Article',
        ),
    ]
