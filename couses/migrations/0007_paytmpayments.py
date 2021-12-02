# Generated by Django 3.2 on 2021-12-01 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couses', '0006_donation'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaytmPayments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MERCHANT_KEY', models.CharField(max_length=100)),
                ('MID', models.CharField(max_length=100)),
                ('WEBSITE', models.CharField(choices=[(1, 'WEBSTAGING'), (2, 'DEFAULT')], help_text='choose Webstaging for testiing and Default for production', max_length=100)),
            ],
        ),
    ]