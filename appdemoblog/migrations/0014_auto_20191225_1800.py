# Generated by Django 3.0.1 on 2019-12-25 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appdemoblog', '0013_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='appdemoblog.Author', verbose_name='Автор'),
        ),
    ]
