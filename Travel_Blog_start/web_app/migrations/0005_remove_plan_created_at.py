# Generated by Django 5.0.2 on 2024-04-13 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0004_remove_article_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='created_at',
        ),
    ]
