# Generated by Django 3.0.1 on 2019-12-25 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdemoblog', '0003_auto_20191224_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default=1, upload_to='images/posts/', verbose_name='Основное изображение'),
            preserve_default=False,
        ),
    ]
