# Generated by Django 5.1.6 on 2025-03-05 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Personal_Blog_App', '0003_article_edited'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='edited',
        ),
    ]
