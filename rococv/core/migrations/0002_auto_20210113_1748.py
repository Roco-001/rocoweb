# Generated by Django 2.1 on 2021-01-13 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='direccion',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='about',
            name='phone',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Teléfono'),
        ),
    ]
