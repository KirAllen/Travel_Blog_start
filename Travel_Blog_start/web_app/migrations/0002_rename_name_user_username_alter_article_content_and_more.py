# Generated by Django 5.0.2 on 2024-04-12 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='plan',
            name='content',
            field=models.TextField(),
        ),
    ]
