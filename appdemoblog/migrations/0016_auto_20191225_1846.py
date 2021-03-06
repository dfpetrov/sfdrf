# Generated by Django 3.0.1 on 2019-12-25 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdemoblog', '0015_auto_20191225_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Описание категории'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название категории'),
        ),
    ]
