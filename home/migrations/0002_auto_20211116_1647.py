# Generated by Django 3.2.9 on 2021-11-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeslider',
            name='shortDiscription',
            field=models.TextField(default='', max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homeslider',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
