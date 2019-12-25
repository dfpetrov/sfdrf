# Generated by Django 3.0.1 on 2019-12-25 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdemoblog', '0012_auto_20191225_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('avatar', models.ImageField(upload_to='appdemoblog/images/authors/', verbose_name='Аватар')),
                ('description', models.TextField(verbose_name='О себе')),
                ('slug', models.SlugField(blank=True, default=None, null=True, unique=True)),
            ],
        ),
    ]
