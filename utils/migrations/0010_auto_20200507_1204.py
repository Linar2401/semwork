# Generated by Django 3.0.5 on 2020-05-07 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0009_auto_20200507_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 7, 12, 4, 44, 509258), verbose_name='Дата публикации'),
        ),
    ]
