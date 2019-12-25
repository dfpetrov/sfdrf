# Generated by Django 3.0.1 on 2019-12-25 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdemoblog', '0004_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='appdemoblog/images/posts/', verbose_name='Основное изображение'),
        ),
    ]