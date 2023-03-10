# Generated by Django 4.1.5 on 2023-01-30 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('example', models.TextField()),
                ('whichChapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.chapter')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='whichLanguage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.language'),
        ),
    ]
