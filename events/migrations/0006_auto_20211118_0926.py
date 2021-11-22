# Generated by Django 3.2.9 on 2021-11-18 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_events_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='country',
            field=models.CharField(default='india', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='events',
            name='zip',
            field=models.CharField(default=452010, max_length=10),
            preserve_default=False,
        ),
    ]