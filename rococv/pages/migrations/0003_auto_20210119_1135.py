# Generated by Django 2.1 on 2021-01-19 17:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210118_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contenido'),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/blog', verbose_name='Imagen'),
        ),
    ]
