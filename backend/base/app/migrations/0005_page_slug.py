# Generated by Django 4.1.5 on 2023-01-31 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_chapter_whichlanguage_delete_python'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
