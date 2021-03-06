# Generated by Django 3.2 on 2021-12-01 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couses', '0008_rename_paytmpayments_paytmconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='paytmconfig',
            name='activate',
            field=models.BooleanField(default=False, help_text=':- check to activate'),
        ),
        migrations.AddField(
            model_name='paytmconfig',
            name='title',
            field=models.CharField(default='testing', help_text='add mode for example "( testing config )" ', max_length=100),
            preserve_default=False,
        ),
    ]
