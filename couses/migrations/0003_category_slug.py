# Generated by Django 3.2.9 on 2021-11-17 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couses', '0002_couses_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
