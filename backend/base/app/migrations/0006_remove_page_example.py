# Generated by Django 4.1.5 on 2023-02-01 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_page_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='example',
        ),
    ]
