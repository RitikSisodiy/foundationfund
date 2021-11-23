# Generated by Django 3.2.9 on 2021-11-22 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=40)),
                ('resume', models.FileField(upload_to='resume')),
                ('status', models.CharField(choices=[('Applied', 'Applied'), ('Reviewed', 'Reviewed'), ('Pending', 'Pending'), ('Verified', 'Verified')], default='Applied', max_length=20)),
            ],
        ),
    ]