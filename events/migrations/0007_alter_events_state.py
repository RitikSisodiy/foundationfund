# Generated by Django 3.2.9 on 2021-11-18 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20211118_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
