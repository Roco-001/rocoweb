# Generated by Django 2.1 on 2021-01-14 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_curso_certificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('cargo', models.CharField(max_length=100, verbose_name='Cargo')),
                ('referencia', models.CharField(max_length=100, verbose_name='Referencia')),
                ('testimonio', models.CharField(max_length=100, verbose_name='Testimonio')),
                ('firma', models.CharField(max_length=100, verbose_name='Nombre de la Firma')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Referencia',
                'verbose_name_plural': 'Referencias',
            },
        ),
    ]
