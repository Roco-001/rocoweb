# Generated by Django 2.1 on 2021-01-14 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210113_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.CharField(max_length=100, verbose_name='Tiempo')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del Curso')),
                ('academia', models.CharField(max_length=100, verbose_name='Academia')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.CharField(max_length=100, verbose_name='Tiempo')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo Obtenido')),
                ('universidad', models.CharField(max_length=100, verbose_name='Universidad')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Educacion',
                'verbose_name_plural': 'Educacion',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la Habilidad')),
                ('porcentaje', models.CharField(max_length=100, verbose_name='Porcentaje')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
            },
        ),
    ]
