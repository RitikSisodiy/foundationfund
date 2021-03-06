# Generated by Django 3.2.9 on 2021-11-23 11:35

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('couses', '0005_alter_couses_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('News', 'News'), ('Blog', 'Blog')], max_length=5)),
                ('time', models.DateTimeField(auto_now=True)),
                ('img', models.ImageField(upload_to='News-Blog')),
                ('titie', models.CharField(max_length=150)),
                ('shortDes', models.CharField(max_length=200)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.SlugField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Blog', to='couses.category')),
            ],
        ),
    ]
