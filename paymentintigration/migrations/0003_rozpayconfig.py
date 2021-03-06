# Generated by Django 3.2.9 on 2021-12-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentintigration', '0002_paytmconfig_posturl'),
    ]

    operations = [
        migrations.CreateModel(
            name='rozpayConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='add mode for example "( testing config )" ', max_length=100)),
                ('activate', models.BooleanField(default=False, help_text=':- check to activate')),
                ('RAZOR_KEY_ID', models.CharField(max_length=200)),
                ('RAZOR_KEY_SECRET', models.CharField(max_length=200)),
            ],
        ),
    ]
